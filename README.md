# iiot6-webapp-suite

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

A comprehensive suite of frontend web applications developed as part of the Phase 1 coursework for B.Tech Computer Science & Engineering (IIOT-6), Invertis University, 6th Semester. These projects are designed to address real-world scenarios in the Industrial Internet of Things (IIOT) curriculum.

---

## Table of Contents

- [Introduction](#introduction)
- [Project List](#project-list)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Folder Structure](#folder-structure)
- [Deployment](#deployment)
- [Future Roadmap](#future-roadmap)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)

---

## Introduction

This repository, **iiot6-webapp-suite**, contains a comprehensive collection of **14 professional web applications** built to demonstrate practical skills in frontend development, backend integration, and modern web technologies. The suite is structured in phases to reflect a real-world software development lifecycle, making it suitable for both academic evaluation and professional portfolio presentation.

## 📊 Project Statistics

- **🌐 Total Applications**: 14 Complete Web Applications ✅
  - 🏥 **Healthcare**: Clinic, Fitness (2 apps)
  - 🏨 **Business**: Hotel, Restaurant, Online Store (3 apps)  
  - 🏢 **Professional**: Lawyer, Interior Design (2 apps)
  - 🏫 **Education**: School, NGO Charity (2 apps)
  - 📰 **Media**: Blog, News, Portfolio (3 apps)
  - 🚀 **Technology**: Startup, Travel (2 apps)
- **📄 HTML Templates**: 90+ Responsive Pages
- **🎨 CSS/JS Libraries**: Bootstrap, Font Awesome, Owl Carousel, Animate.css
- **⚙️ Flask Routes**: 50+ Properly Configured Routes
- **📱 Responsive Design**: 100% Mobile-First Approach
- **🚀 Deployment Ready**: All Apps Configured for Cloud Deployment
- **📖 Documentation**: Individual README for Each Project

---


## Project List

### 🏥 Healthcare & Wellness
- **Clinic WebApp** ([README](ClinicWebApp/README.md)) - Professional healthcare clinic website with appointment booking, services showcase, team profiles, and patient testimonials
- **Fitness WebApp** ([README](FitnessWebApp/README.md)) - Modern fitness center website with course catalog, trainer profiles, membership info, and workout programs

### 🏨 Business & Hospitality  
- **Hotel WebApp** ([README](HotelWebApp/README.md)) - Complete hotel booking platform with room listings, services, amenities, and reservation system
- **Restaurant WebApp** ([README](ResturantsWebApp/README.md)) - Full-featured restaurant website with menu display, table reservations, chef profiles, and contact forms
- **Online Store WebApp** ([README](OnlineStoreWebApp/README.md)) - E-commerce platform with product catalog, shopping cart, checkout process, and customer support

### 🏢 Professional Services
- **Lawyer WebApp** ([README](LawyerWebApp/README.md)) - Professional law firm website with practice areas, attorney profiles, case studies, and consultation booking
- **Interior Design WebApp** ([README](InteriorDesignWebApp/README.md)) - Portfolio website for interior designers with project galleries, services, and client testimonials

### 🏫 Education & Non-Profit
- **School WebApp** ([README](SchoolWebApp/README.md)) - Comprehensive educational institution website with courses, faculty, admissions, and academic programs
- **NGO Charity WebApp** ([README](NGOCharityWebApp/README.md)) - Charity organization website with donation campaigns, volunteer programs, and impact stories

### 📰 Media & Portfolio
- **Blog WebApp** ([README](BlogWebApp/README.md)) - Modern blog platform with article publishing, categories, author profiles, and content management
- **News WebApp** ([README](NewsWebApp/README.md)) - Professional news and media website with article display, categories, and breaking news sections
- **Portfolio WebApp** ([README](PortfolioWebApp/README.md)) - Personal portfolio showcase for professionals, artists, and freelancers

### 🚀 Technology & Travel
- **Startup WebApp** ([README](StartupWebApp/README.md)) - Modern startup company website with product showcase, team profiles, and investor information
- **Travel WebApp** ([README](TravelWebApp/README.md)) - Travel and tourism platform with destination guides, booking services, and travel blog

---

## Features

- ✅ **Complete Flask Applications**: All 14 web applications with fully implemented routes and templates
- 🎨 **Responsive Design**: Modern, mobile-first responsive designs using Bootstrap
- 🔗 **Flask Integration**: Proper Flask `url_for()` usage for static files and routing
- 📱 **Cross-platform Compatibility**: Ready for deployment on various cloud platforms
- 🚀 **Easy Deployment**: Configured for Render.com, Heroku, and other PaaS platforms
- 📝 **Complete Documentation**: Individual README files for each project
- 🎯 **Industry-Specific Themes**: Healthcare, Business, Education, Media, and more
- 🛠️ **Modular Structure**: Clean separation of templates, static files, and application logic

---

## Technologies Used

### Backend Framework
- **Flask (Python)** - Lightweight and flexible web framework
- **Jinja2 Templates** - Dynamic HTML rendering
- **Werkzeug WSGI** - Web server gateway interface

### Frontend Technologies
- **HTML5** - Modern semantic markup
- **CSS3** - Advanced styling with Flexbox and Grid
- **JavaScript (ES6+)** - Interactive functionality
- **Bootstrap 5** - Responsive CSS framework
- **jQuery** - DOM manipulation and AJAX

### UI/UX Libraries
- **Font Awesome** - Icon library
- **Bootstrap Icons** - Additional icon sets  
- **Animate.css** - CSS animations
- **Owl Carousel** - Image and content carousels
- **Lightbox** - Image galleries
- **Tempus Dominus** - Date/time pickers

### Development Tools
- **Git** - Version control
- **VS Code** - Development environment
- **Chrome DevTools** - Debugging and testing

### Deployment Platforms
- **Render.com** - Primary deployment platform
- **Heroku** - Alternative cloud platform
- **PythonAnywhere** - Python-specific hosting
- **Netlify** - Static site deployment option

---

## Quick Start

To run any of the web applications:

1. **Navigate to the desired app folder:**
   ```bash
   cd ClinicWebApp  # or any other app folder
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open in browser:**
   ```
   http://localhost:5000
   ```

Each application runs independently with its own Flask server and can be deployed separately.

### 🛠️ Development Mode
To run with auto-reload for development:
```bash
export FLASK_ENV=development  # Linux/Mac
set FLASK_ENV=development     # Windows
python app.py
```

### 🧪 Testing Applications
Test any application quickly:
```bash
cd [AppName]WebApp
python -c "from app import app; print('✅ App imported successfully!')"
```

---

## 🏗️ Project Architecture

### Application Structure
Each web application follows a consistent, industry-standard structure:

```
[AppName]WebApp/
├── 📄 app.py                 # Flask application with routes
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md             # Application documentation
├── 📁 static/               # Static assets
│   ├── 🎨 css/              # Stylesheets
│   ├── 🖼️  img/              # Images and icons
│   ├── ⚡ js/               # JavaScript files
│   ├── 📚 lib/              # Third-party libraries
│   └── 📧 mail/             # Email templates (where applicable)
└── 📁 templates/            # HTML templates
    ├── 🏠 index.html        # Homepage
    ├── 📝 about.html        # About page
    ├── 📞 contact.html      # Contact page
    └── 📄 [other].html      # Feature-specific pages
```

### Flask Application Pattern
- **Route-based URLs**: Clean, SEO-friendly URL structure
- **Template Inheritance**: Consistent styling across pages
- **Static File Handling**: Proper Flask `url_for()` integration
- **Error Handling**: 404 pages where applicable
- **Responsive Design**: Mobile-first approach

## Folder Structure

```
iiot6-webapp-suite/
│
├── BlogWebApp/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── static/
│   └── templates/
│
├── ClinicWebApp/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── static/
│   └── templates/
│
├── FitnessWebApp/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── static/
│   └── templates/
│
├── HotelWebApp/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── static/
│   └── templates/
│
├── InteriorDesignWebApp/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── static/
│   └── templates/
│
├── LawyerWebApp/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── static/
│   └── templates/
│
├── NewsWebApp/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── static/
│   └── templates/
│
├── NGOCharityWebApp/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── static/
│   └── templates/
│
├── OnlineStoreWebApp/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── static/
│   └── templates/
│
├── PortfolioWebApp/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── static/
│   └── templates/
│
├── ResturantsWebApp/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── static/
│   └── templates/
│
├── SchoolWebApp/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── static/
│   └── templates/
│
├── StartupWebApp/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── static/
│   └── templates/
│
├── TravelWebApp/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── static/
│   └── templates/
│
└── README.md
```

---

## Deployment

All web applications in this suite are production-ready and configured for deployment on multiple cloud platforms.

### 🔧 Deployment Options

#### Option 1: Render.com (Recommended)
1. Push the desired project folder to a GitHub repository
2. Connect your repository to [Render.com](https://render.com/)
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python app.py`
5. Configure environment variables if needed

#### Option 2: Heroku
1. Install Heroku CLI and login
2. Create a new Heroku app: `heroku create your-app-name`
3. Push to Heroku: `git push heroku main`
4. Open your app: `heroku open`

#### Option 3: PythonAnywhere
1. Upload your project files to PythonAnywhere
2. Set up a web app with Flask
3. Configure WSGI file to point to your app.py
4. Reload your web app

### 📦 Deployment Requirements
- Python 3.8+
- Flask (specified in requirements.txt)
- Access to static files (CSS, JS, Images)
- Port configuration (default: 5000)

---

## Future Roadmap

- **Phase 2:** Integrate backend logic and connect to databases for dynamic content management.
- **Phase 3:** Incorporate AI tools such as chatbots, recommendation systems, and automation features.
- Add comprehensive test suites for all applications.
- Enhance UI/UX with modern frameworks and design systems.
- Expand documentation and add user guides.

---

## Contribution Guidelines

We welcome contributions from students and the open-source community!

- Fork the repository and create your branch (`git checkout -b feature/YourFeature`)
- Commit your changes (`git commit -am 'Add new feature'`)
- Push to the branch (`git push origin feature/YourFeature`)
- Open a Pull Request with a clear description

Please follow the existing code style and add documentation where necessary.

---

## 🎓 Academic Context

**Course**: B.Tech Computer Science & Engineering (IIOT-6)  
**Institution**: Invertis University  
**Semester**: 6th Semester  
**Project Phase**: Phase 1 - Frontend Development & Flask Integration  

### Learning Objectives Achieved
- ✅ Modern Web Development with Flask
- ✅ Responsive UI/UX Design Principles  
- ✅ Industry-Standard Project Structure
- ✅ Version Control & Documentation
- ✅ Cloud Deployment Practices
- ✅ Professional Portfolio Development

### Next Phases
- **Phase 2**: Database Integration & Backend Logic
- **Phase 3**: AI/ML Integration & Automation

---

## 📞 Support

For questions, issues, or contributions:
- 📧 **Email**: Contact through university portal
- 📖 **Documentation**: Check individual README files
- 🐛 **Issues**: Open GitHub issues for bugs
- 💡 **Ideas**: Submit feature requests

---

## License

This project is intended for academic and educational purposes. For other uses, please contact the repository maintainers @Arya182-ui

---
