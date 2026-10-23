# Smart Hospital Management + Disease Prediction

A final-year/demo Django project combining hospital management with a machine-learning
disease prediction module.

## Main Modules
- Dashboard
- Patient registration and patient list
- Doctor management
- Appointment management
- Disease prediction from symptoms
- Prediction history
- Admin panel
- Responsive Bootstrap-style UI using local CSS (no internet required)

## Important
The disease predictor is an educational/demo ML feature. It is **not a medical diagnosis**
and should not be used for real clinical decisions.

## Setup

### 1. Create/activate virtual environment
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install packages
```bash
pip install -r requirements.txt
```

### 3. Create database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Train the demo ML model
```bash
python ml/train_model.py
```

### 5. Create admin user
```bash
python manage.py createsuperuser
```

### 6. Run server
```bash
python manage.py runserver
```

Open:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/

## Demo Prediction
Go to **Disease Prediction**, select symptoms and submit.
The model predicts one of the diseases in the included educational dataset.

## Project Structure
```
smart_hospital/
├── manage.py
├── requirements.txt
├── db.sqlite3 (created after migrate)
├── ml/
│   ├── dataset.csv
│   ├── train_model.py
│   └── disease_model.joblib (created by training)
├── hospital/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
├── smart_hospital/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── static/css/style.css
```

## Technologies
Python, Django, SQLite, HTML, CSS, JavaScript, scikit-learn, pandas, joblib.
