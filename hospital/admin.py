from django.contrib import admin
from .models import Patient, Doctor, Appointment, DiseasePrediction

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "gender", "phone", "blood_group", "created_at")
    search_fields = ("name", "phone", "email")

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "specialization", "phone", "room_no")
    search_fields = ("name", "specialization")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "doctor", "appointment_date", "status")
    list_filter = ("status",)

@admin.register(DiseasePrediction)
class DiseasePredictionAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "predicted_disease", "confidence", "created_at")
    list_filter = ("predicted_disease",)
