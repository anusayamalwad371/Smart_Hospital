# 🏥 Smart Hospital Management + Disease Prediction

> An intelligent Django-based hospital management system integrated with a Machine Learning disease prediction module for educational and demonstration purposes.

---

## 📌 Project Overview

Smart Hospital Management + Disease Prediction is a  demo web application developed using Python and Django.

The system combines essential hospital management functionalities with an **educational Machine Learning module** that predicts a possible disease based on selected symptoms.

The application provides a centralized platform for managing:

- 👨‍⚕️ Doctors
- 🧑‍🤝‍🧑 Patients
- 📅 Appointments
- 🩺 Disease Prediction
- 📊 Prediction History
- 🔐 Admin Management

The project demonstrates how **Web Development + Database Management + Machine Learning** can be integrated into a single real-world application.

> ⚠️ **Medical Disclaimer:** The disease prediction feature is strictly an educational/demo ML feature. It is **not a medical diagnosis** and must not be used for real clinical decisions.

---

# 🎯 Objectives

The main objectives of this project are:

- Develop a centralized hospital management system.
- Digitize patient and doctor information.
- Manage appointments efficiently.
- Provide an interactive disease prediction module.
- Demonstrate integration of Machine Learning with Django.
- Store prediction history for demonstration and analysis.
- Provide a simple and responsive user interface.
- Build a practical final-year project using modern technologies.

---

# 🚀 Key Features

## 📊 1. Hospital Dashboard

A centralized dashboard provides an overview of the hospital system.

### Dashboard includes:

- Total Patients
- Total Doctors
- Total Appointments
- Recent Appointments
- Disease Prediction statistics

---

## 🧑‍🤝‍🧑 2. Patient Management

The system allows authorized users to manage patient records.

### Features:

- Patient registration
- Patient list
- Patient details
- Contact information
- Medical information
- Patient record management

---

## 👨‍⚕️ 3. Doctor Management

Manage doctor information through the hospital system.

### Features:

- Add doctor
- View doctors
- Doctor specialization
- Contact details
- Doctor availability information

---

## 📅 4. Appointment Management

The appointment module helps organize patient-doctor appointments.

### Features:

- Book appointments
- View appointments
- Patient-doctor mapping
- Appointment date and time
- Appointment status

---

# 🤖 5. AI Disease Prediction

The most important feature of the project is the **Machine Learning-based Disease Prediction module**.

Users can select symptoms from the available list and submit them to the ML model.

### Prediction Workflow

```text
User Selects Symptoms
        ↓
Django Prediction Form
        ↓
Feature Processing
        ↓
Trained ML Model
        ↓
Disease Prediction
        ↓
Prediction Result
        ↓
Prediction History
```

The trained model is loaded by Django and used to generate predictions based on the selected symptoms.

---

# 🧠 Machine Learning Module

The ML module is implemented using **Python and Scikit-learn**.

### ML Pipeline

```text
Dataset
   ↓
Data Preprocessing
   ↓
Feature Selection
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Serialization
   ↓
Django Integration
   ↓
Disease Prediction
```

The trained model is saved using `joblib` and loaded by the Django application during prediction.

### ML Components

- Dataset preparation
- Feature encoding
- Model training
- Prediction
- Model serialization
- Django integration

---

# 🗂️ Prediction History

Every prediction can be stored for demonstration and analysis.

The history can contain:

- Selected symptoms
- Predicted disease
- Prediction date/time
- Patient-related information where applicable

This demonstrates how an ML prediction system can be integrated with a database-backed web application.

---

# 🔐 Admin Panel

The project uses Django's built-in administration system.

Admin users can manage:

- Patients
- Doctors
- Appointments
- Prediction records
- Application data

Access:

```text
http://127.0.0.1:8000/admin/
```

---

# 🎨 User Interface

The application uses a clean, responsive interface based on:

- HTML5
- CSS3
- Bootstrap-style responsive design
- Django Templates

The project uses local CSS assets, so the core UI does not require an internet connection.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| Scikit-learn | Machine Learning |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Joblib | ML model serialization |
| SQLite | Database |
| HTML5 | Frontend |
| CSS3 | Styling |
| Bootstrap-style UI | Responsive design |

---

# 📁 Project Structure

```text
smart_hospital/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── ml/
│   ├── dataset.csv
│   ├── train_model.py
│   └── disease_model.joblib
│
├── hospital/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   │
│   └── templates/
│       ├── base.html
│       ├── dashboard.html
│       ├── patients/
│       ├── doctors/
│       ├── appointments/
│       └── prediction/
│
├── smart_hospital/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
└── static/
    └── css/
        └── style.css
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/smart-hospital-disease-prediction.git
```

Navigate to the project:

```bash
cd smart-hospital-disease-prediction
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create Database

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5️⃣ Train the ML Model

Run:

```bash
python ml/train_model.py
```

This generates the trained model:

```text
ml/disease_model.joblib
```

---

## 6️⃣ Create Admin Account

```bash
python manage.py createsuperuser
```

Enter:

```text
Username
Email
Password
```

---

## 7️⃣ Start Django Server

```bash
python manage.py runserver
```

Open the application:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

---

# 🧪 Example Usage

### Disease Prediction

1. Open the application.
2. Navigate to **Disease Prediction**.
3. Select the patient's symptoms.
4. Submit the prediction form.
5. The ML model processes the selected symptoms.
6. A predicted disease is displayed.
7. The prediction can be stored in prediction history.

---

# 📈 Future Enhancements

The project can be extended with:

- 🔐 Role-based authentication
- 👨‍⚕️ Doctor login portal
- 🧑‍🤝‍🧑 Patient login portal
- 📧 Appointment email notifications
- 📱 Mobile-friendly interface
- 📊 Advanced analytics dashboard
- 📄 Digital medical reports
- 💊 Prescription management
- 🧠 Multiple ML algorithms comparison
- 📈 Model accuracy dashboard
- 🔍 Patient search and filtering
- ☁️ Cloud deployment
- 🔗 REST API integration
- 🗄️ PostgreSQL/MySQL support

---

# 🎓 Academic Relevance

This project demonstrates practical knowledge of:

### Python

- Object-oriented programming
- Functions
- File handling
- Data processing
- Exception handling

### Django

- Models
- Views
- Forms
- Templates
- URLs
- Admin panel
- Database integration

### Machine Learning

- Dataset preprocessing
- Feature engineering
- Model training
- Prediction
- Model serialization

### Database

- CRUD operations
- Relational data management
- SQLite integration

### Web Development

- HTML
- CSS
- Responsive UI
- Django template system

---

# 💼 Skills Demonstrated

This project demonstrates hands-on skills in:

```text
Python
Django
Machine Learning
Scikit-learn
Pandas
NumPy
SQLite
HTML
CSS
CRUD Operations
Database Management
Model Deployment
Git & GitHub
```

---

# ⚠️ Disclaimer

This project is created for **educational, academic, and demonstration purposes only**.

The Machine Learning disease prediction feature provides an experimental prediction based on the training dataset.

It:

- ❌ Does not provide medical diagnosis.
- ❌ Does not replace a qualified healthcare professional.
- ❌ Should not be used for clinical decisions.
- ❌ Should not be used for emergency medical situations.

Always consult a qualified healthcare professional for medical advice and diagnosis.

---

# 👩‍💻 Author

Anusaya Malwad
 MCA-2028  
💻 Python | Django | Machine Learning | Data Analytics

---



## 🔖 Project Tags

```text
django
python
machine-learning
disease-prediction
hospital-management-system
healthcare
scikit-learn
sqlite
pandas
numpy
web-development

django-ml-project
ai-healthcare
```
