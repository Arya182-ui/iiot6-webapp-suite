# 🌐 IIOT-6 MasterWebApp

**All 14 Websites in One Application!**

This is a unified Flask application that combines all 14 individual web applications into a single deployable unit. Instead of hosting 14 separate apps, you can now deploy just **one app** and access all websites through different routes.

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the master app
python app.py

# Open in browser
http://localhost:5000
```

## 🌟 What You Get

### **Single Deployment Solution**
- ✅ **One App** = All 14 Websites
- ✅ **One Domain** = Multiple Projects  
- ✅ **One Deployment** = Save Time & Money
- ✅ **Professional Landing Page** with Navigation

### **All Websites Included:**

| Route | Website | Description |
|-------|---------|-------------|
| `/clinic/` | Clinic WebApp | Healthcare clinic with appointments |
| `/fitness/` | Fitness WebApp | Gym and fitness center |
| `/hotel/` | Hotel WebApp | Hotel booking platform |
| `/restaurant/` | Restaurant WebApp | Restaurant with menu & reservations |
| `/store/` | Online Store | E-commerce shopping platform |
| `/lawyer/` | Lawyer WebApp | Law firm website |
| `/interior/` | Interior Design | Design portfolio |
| `/school/` | School WebApp | Educational institution |
| `/ngo/` | NGO Charity | Charity organization |
| `/blog/` | Blog WebApp | Blog and articles |
| `/news/` | News WebApp | News and media |
| `/portfolio/` | Portfolio WebApp | Personal portfolio |
| `/startup/` | Startup WebApp | Startup company |
| `/travel/` | Travel WebApp | Travel and tourism |

## 📁 Structure

```
MasterWebApp/
├── 📄 app.py                    # Main Flask application
├── 📄 requirements.txt          # Dependencies  
├── 📄 setup_master_app.py       # Setup script (copies files)
├── 📄 README.md                # This file
├── 📁 templates/
│   ├── 🏠 master_index.html    # Beautiful landing page
│   ├── 📁 blog/                # Blog app templates
│   ├── 📁 clinic/              # Clinic app templates
│   ├── 📁 fitness/             # Fitness app templates
│   └── 📁 [all other apps]/    # All other app templates
└── 📁 static/
    ├── 📁 blog/                # Blog app static files
    ├── 📁 clinic/              # Clinic app static files  
    ├── 📁 fitness/             # Fitness app static files
    └── 📁 [all other apps]/    # All other app static files
```

## 🔧 How It Works

1. **Unified Routes**: Each website gets its own URL prefix (e.g., `/clinic/`, `/hotel/`)
2. **Template Organization**: Templates are organized by app in separate folders
3. **Static File Handling**: Each app's CSS, JS, images are in separate static folders  
4. **Landing Page**: Beautiful homepage showing all available websites
5. **Easy Navigation**: Click any card to visit that specific website

## 🌐 Deployment Benefits

### **Instead of This** ❌:
- Deploy 14 separate apps
- Manage 14 different domains
- Pay for 14 hosting services
- Monitor 14 different deployments

### **You Get This** ✅:
- Deploy **1 master app**
- Use **1 domain** with different routes
- Pay for **1 hosting service**  
- Monitor **1 deployment**

## 🚀 Deployment Instructions

### **Render.com (Recommended)**
1. Push this MasterWebApp folder to GitHub
2. Connect to Render.com
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python app.py`
5. Deploy! 🎉

### **Heroku**
```bash
# In MasterWebApp folder
heroku create your-master-app-name
git add .
git commit -m "Deploy master app"
git push heroku main
heroku open
```

### **Other Platforms**
Works on any Python hosting platform:
- PythonAnywhere
- Railway
- Fly.io
- DigitalOcean App Platform

## 🔄 Updating Content

If you modify any individual app:

1. Run the setup script to sync changes:
   ```bash
   python setup_master_app.py
   ```

2. Redeploy the master app

## 🎯 Perfect For

- **Students**: Submit all projects in one deployment
- **Portfolio**: Show all your work in one place  
- **Demos**: Easy to showcase multiple projects
- **Cost Savings**: One hosting fee instead of many

## 💡 Pro Tips

- **Custom Domain**: Point your domain to the master app
- **Subdirectories**: Each website feels like a separate site
- **Professional**: Landing page looks amazing for presentations
- **SEO Friendly**: Each route can be indexed separately

---

**🎓 Invertis University - B.Tech CSE (IIOT-6) - 6th Semester**  
*Phase 1: Frontend Development & Flask Integration*