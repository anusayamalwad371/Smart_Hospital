from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("patients/", views.patient_list, name="patient_list"),
    path("patients/add/", views.patient_add, name="patient_add"),
    path("doctors/", views.doctor_list, name="doctor_list"),
    path("doctors/add/", views.doctor_add, name="doctor_add"),
    path("appointments/", views.appointment_list, name="appointment_list"),
    path("appointments/add/", views.appointment_add, name="appointment_add"),
    path("predict/", views.predict_disease, name="predict_disease"),
    path("predictions/", views.prediction_history, name="prediction_history"),
]
