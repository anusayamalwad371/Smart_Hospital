from pathlib import Path
import joblib
import numpy as np

from django.contrib import messages
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PatientForm, DoctorForm, AppointmentForm
from .models import Patient, Doctor, Appointment, DiseasePrediction

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "ml" / "disease_model.joblib"

SYMPTOMS = [
    "fever", "cough", "fatigue", "headache", "body_pain",
    "sore_throat", "runny_nose", "shortness_of_breath",
    "nausea", "vomiting", "diarrhea", "abdominal_pain",
    "chest_pain", "dizziness", "loss_of_smell", "loss_of_taste",
    "joint_pain", "skin_rash", "itching", "frequent_urination",
]

def _model():
    if not MODEL_PATH.exists():
        return None
    return joblib.load(MODEL_PATH)

def dashboard(request):
    context = {
        "patient_count": Patient.objects.count(),
        "doctor_count": Doctor.objects.count(),
        "appointment_count": Appointment.objects.count(),
        "prediction_count": DiseasePrediction.objects.count(),
        "upcoming": Appointment.objects.select_related("patient", "doctor").order_by("appointment_date")[:5],
        "recent_predictions": DiseasePrediction.objects.select_related("patient").order_by("-created_at")[:5],
    }
    return render(request, "dashboard.html", context)

def patient_list(request):
    q = request.GET.get("q", "").strip()
    patients = Patient.objects.all().order_by("-created_at")
    if q:
        patients = patients.filter(name__icontains=q)
    return render(request, "patients.html", {"patients": patients, "q": q})

def patient_add(request):
    form = PatientForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Patient registered successfully.")
        return redirect("patient_list")
    return render(request, "form.html", {"form": form, "title": "Register Patient", "back": "patient_list"})

def doctor_list(request):
    doctors = Doctor.objects.all().order_by("name")
    return render(request, "doctors.html", {"doctors": doctors})

def doctor_add(request):
    form = DoctorForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Doctor added successfully.")
        return redirect("doctor_list")
    return render(request, "form.html", {"form": form, "title": "Add Doctor", "back": "doctor_list"})

def appointment_list(request):
    appointments = Appointment.objects.select_related("patient", "doctor").order_by("-appointment_date")
    return render(request, "appointments.html", {"appointments": appointments})

def appointment_add(request):
    form = AppointmentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Appointment created successfully.")
        return redirect("appointment_list")
    return render(request, "form.html", {"form": form, "title": "Create Appointment", "back": "appointment_list"})

def predict_disease(request):
    result = None
    confidence = None
    selected = []

    if request.method == "POST":
        selected = request.POST.getlist("symptoms")
        model = _model()
        if model is None:
            messages.error(request, "ML model not found. Run: python ml/train_model.py")
        elif not selected:
            messages.warning(request, "Please select at least one symptom.")
        else:
            vector = np.array([[1 if s in selected else 0 for s in SYMPTOMS]])
            result = model["model"].predict(vector)[0]
            probabilities = model["model"].predict_proba(vector)[0]
            confidence = round(float(max(probabilities)) * 100, 2)
            patient_id = request.POST.get("patient")
            patient = Patient.objects.filter(id=patient_id).first() if patient_id else None
            DiseasePrediction.objects.create(
                patient=patient,
                symptoms=", ".join(selected),
                predicted_disease=result,
                confidence=confidence,
            )

    return render(
        request,
        "predict.html",
        {
            "symptoms": SYMPTOMS,
            "selected": selected,
            "result": result,
            "confidence": confidence,
            "patients": Patient.objects.all().order_by("name"),
        },
    )

def prediction_history(request):
    predictions = DiseasePrediction.objects.select_related("patient").order_by("-created_at")
    return render(request, "predictions.html", {"predictions": predictions})
