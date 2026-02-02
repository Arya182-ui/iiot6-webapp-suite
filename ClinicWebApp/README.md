# Clinic WebApp

A modern, responsive healthcare clinic website built with Flask as part of the IIOT-6 WebApp Suite (Invertis University, 6th Semester).

## Features
- Home, About, Services, Appointment, Team, Features, Testimonial, Contact pages
- Responsive design using Bootstrap
- Healthcare-focused UI with professional styling
- Easy to deploy and customize

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone this repository or copy the ClinicWebApp folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open your browser at http://localhost:5000

## Project Structure
```
ClinicWebApp/
├── app.py
├── requirements.txt
├── static/
│   ├── css/
│   ├── img/
│   ├── js/
│   ├── lib/
│   └── scss/
└── templates/
    ├── index.html
    ├── about.html
    ├── service.html
    ├── appointment.html
    ├── team.html
    ├── feature.html
    ├── testimonial.html
    ├── contact.html
    └── 404.html
```

## Technologies Used
- Python (Flask)
- HTML, CSS, JavaScript
- Bootstrap
- SCSS for styling

## Deployment
This app is ready to deploy on platforms like:
- Render.com
- Heroku
- PythonAnywhere

## Future Enhancements
- Database integration for appointments
- Patient management system
- Online consultation features
- Payment gateway integration