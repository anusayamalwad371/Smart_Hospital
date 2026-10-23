from django import forms
from .models import Patient, Doctor, Appointment

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name", "age", "gender", "phone", "email", "blood_group", "address"]
        widgets = {
            "address": forms.Textarea(attrs={"rows": 3}),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ["name", "specialization", "phone", "email", "room_no"]

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["patient", "doctor", "appointment_date", "reason", "status"]
        widgets = {
            "appointment_date": forms.DateTimeInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["appointment_date"].input_formats = ["%Y-%m-%dT%H:%M"]
