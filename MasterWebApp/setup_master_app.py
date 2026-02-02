import os
import shutil
import sys

def copy_templates_and_static():
    """Copy all templates and static files from individual apps to MasterWebApp"""
    
    base_dir = r"d:\IIOT_6"
    master_dir = os.path.join(base_dir, "MasterWebApp")
    
    # Create directories
    templates_dir = os.path.join(master_dir, "templates")
    static_dir = os.path.join(master_dir, "static")
    
    os.makedirs(templates_dir, exist_ok=True)
    os.makedirs(static_dir, exist_ok=True)
    
    # Web app mappings
    apps = {
        'blog': 'BlogWebApp',
        'clinic': 'ClinicWebApp', 
        'fitness': 'FitnessWebApp',
        'hotel': 'HotelWebApp',
        'interior': 'InteriorDesignWebApp',
        'lawyer': 'LawyerWebApp',
        'news': 'NewsWebApp',
        'ngo': 'NGOCharityWebApp',
        'store': 'OnlineStoreWebApp',
        'portfolio': 'PortfolioWebApp',
        'restaurant': 'ResturantsWebApp',
        'school': 'SchoolWebApp',
        'startup': 'StartupWebApp',
        'travel': 'TravelWebApp'
    }
    
    print("🚀 Starting to copy templates and static files...")
    
    for short_name, full_name in apps.items():
        app_path = os.path.join(base_dir, full_name)
        
        if os.path.exists(app_path):
            # Copy templates
            src_templates = os.path.join(app_path, "templates")
            dst_templates = os.path.join(templates_dir, short_name)
            
            if os.path.exists(src_templates):
                if os.path.exists(dst_templates):
                    shutil.rmtree(dst_templates)
                shutil.copytree(src_templates, dst_templates)
                print(f"✅ Copied templates: {full_name} -> {short_name}")
            
            # Copy static files
            src_static = os.path.join(app_path, "static")
            dst_static = os.path.join(static_dir, short_name)
            
            if os.path.exists(src_static):
                if os.path.exists(dst_static):
                    shutil.rmtree(dst_static)
                shutil.copytree(src_static, dst_static)
                print(f"📁 Copied static files: {full_name} -> {short_name}")
        else:
            print(f"❌ App not found: {full_name}")
    
    print(f"\n🎉 All files copied to MasterWebApp!")
    print(f"📍 Location: {master_dir}")
    print(f"🌐 Run with: cd MasterWebApp && python app.py")

if __name__ == "__main__":
    copy_templates_and_static()