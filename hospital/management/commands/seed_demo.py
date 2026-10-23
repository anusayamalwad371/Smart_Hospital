from django.core.management.base import BaseCommand
from hospital.models import Patient, Doctor, Appointment
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = "Create demo patients, doctors and appointments"

    def handle(self, *args, **options):
        doctors = [
            ("Aarav Sharma", "General Medicine", "9876500011", "aarav@example.com", "101"),
            ("Meera Patil", "Cardiology", "9876500012", "meera@example.com", "202"),
            ("Rohan Kulkarni", "Neurology", "9876500013", "rohan@example.com", "303"),
        ]
        for data in doctors:
            Doctor.objects.get_or_create(name=data[0], defaults={
                "specialization": data[1], "phone": data[2], "email": data[3], "room_no": data[4]
            })

        patients = [
            ("Ananya Deshmukh", 24, "Female", "9000000001", "ananya@example.com", "O+"),
            ("Rahul Patil", 31, "Male", "9000000002", "rahul@example.com", "B+"),
            ("Sneha Jadhav", 28, "Female", "9000000003", "sneha@example.com", "A+"),
        ]
        objs = []
        for data in patients:
            obj, _ = Patient.objects.get_or_create(name=data[0], defaults={
                "age": data[1], "gender": data[2], "phone": data[3], "email": data[4], "blood_group": data[5]
            })
            objs.append(obj)

        ds = list(Doctor.objects.all()[:3])
        for i, patient in enumerate(objs):
            if ds:
                Appointment.objects.get_or_create(
                    patient=patient, doctor=ds[i % len(ds)],
                    appointment_date=timezone.now() + timedelta(days=i+1),
                    defaults={"reason": "Routine consultation", "status": "Scheduled"}
                )
        self.stdout.write(self.style.SUCCESS("Demo data created."))
