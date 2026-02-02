from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)

# Configure static folder paths
app.static_folder = 'static'
app.static_url_path = '/static'

# Custom static file handler for different apps
@app.route('/static/<app_name>/<path:filename>')
def app_static(app_name, filename):
    return app.send_static_file(f"{app_name}/{filename}")

# Main landing page to show all websites
@app.route('/')
def home():
    return render_template('master_index.html')

# Blog WebApp routes
@app.route('/blog/')
def blog_home():
    return render_template('blog/index.html')

@app.route('/blog/about')
def blog_about():
    return render_template('blog/about.html')

@app.route('/blog/blog')
def blog_blog():
    return render_template('blog/blog.html')

@app.route('/blog/contact')
def blog_contact():
    return render_template('blog/contact.html')

@app.route('/blog/single')
def blog_single():
    return render_template('blog/single.html')

# Clinic WebApp routes
@app.route('/clinic/')
def clinic_home():
    return render_template('clinic/index.html')

@app.route('/clinic/about.html')
def clinic_about():
    return render_template('clinic/about.html')

@app.route('/clinic/service.html')
def clinic_service():
    return render_template('clinic/service.html')

@app.route('/clinic/appointment.html')
def clinic_appointment():
    return render_template('clinic/appointment.html')

@app.route('/clinic/team.html')
def clinic_team():
    return render_template('clinic/team.html')

@app.route('/clinic/feature.html')
def clinic_feature():
    return render_template('clinic/feature.html')

@app.route('/clinic/testimonial.html')
def clinic_testimonial():
    return render_template('clinic/testimonial.html')

@app.route('/clinic/contact.html')
def clinic_contact():
    return render_template('clinic/contact.html')

# Fitness WebApp routes
@app.route('/fitness/')
def fitness_home():
    return render_template('fitness/index.html')

@app.route('/fitness/about.html')
def fitness_about():
    return render_template('fitness/about.html')

@app.route('/fitness/course.html')
def fitness_course():
    return render_template('fitness/course.html')

@app.route('/fitness/team.html')
def fitness_team():
    return render_template('fitness/team.html')

@app.route('/fitness/testimonial.html')
def fitness_testimonial():
    return render_template('fitness/testimonial.html')

@app.route('/fitness/contact.html')
def fitness_contact():
    return render_template('fitness/contact.html')

# Hotel WebApp routes
@app.route('/hotel/')
def hotel_home():
    return render_template('hotel/index.html')

@app.route('/hotel/about.html')
def hotel_about():
    return render_template('hotel/about.html')

@app.route('/hotel/service.html')
def hotel_service():
    return render_template('hotel/service.html')

@app.route('/hotel/room.html')
def hotel_room():
    return render_template('hotel/room.html')

@app.route('/hotel/booking.html')
def hotel_booking():
    return render_template('hotel/booking.html')

@app.route('/hotel/team.html')
def hotel_team():
    return render_template('hotel/team.html')

@app.route('/hotel/testimonial.html')
def hotel_testimonial():
    return render_template('hotel/testimonial.html')

@app.route('/hotel/contact.html')
def hotel_contact():
    return render_template('hotel/contact.html')

# Interior Design WebApp routes
@app.route('/interior/')
def interior_home():
    return render_template('interior/index.html')

@app.route('/interior/about.html')
def interior_about():
    return render_template('interior/about.html')

@app.route('/interior/service.html')
def interior_service():
    return render_template('interior/service.html')

@app.route('/interior/project.html')
def interior_project():
    return render_template('interior/project.html')

@app.route('/interior/team.html')
def interior_team():
    return render_template('interior/team.html')

@app.route('/interior/feature.html')
def interior_feature():
    return render_template('interior/feature.html')

@app.route('/interior/testimonial.html')
def interior_testimonial():
    return render_template('interior/testimonial.html')

@app.route('/interior/contact.html')
def interior_contact():
    return render_template('interior/contact.html')

# Lawyer WebApp routes
@app.route('/lawyer/')
def lawyer_home():
    return render_template('lawyer/index.html')

@app.route('/lawyer/about.html')
def lawyer_about():
    return render_template('lawyer/about.html')

@app.route('/lawyer/service.html')
def lawyer_service():
    return render_template('lawyer/service.html')

@app.route('/lawyer/team.html')
def lawyer_team():
    return render_template('lawyer/team.html')

@app.route('/lawyer/contact.html')
def lawyer_contact():
    return render_template('lawyer/contact.html')

# News WebApp routes
@app.route('/news/')
def news_home():
    return render_template('news/index.html')

@app.route('/news/contact.html')
def news_contact():
    return render_template('news/contact.html')

# NGO Charity WebApp routes
@app.route('/ngo/')
def ngo_home():
    return render_template('ngo/index.html')

@app.route('/ngo/about.html')
def ngo_about():
    return render_template('ngo/about.html')

@app.route('/ngo/donation.html')
def ngo_donation():
    return render_template('ngo/donation.html')

@app.route('/ngo/team.html')
def ngo_team():
    return render_template('ngo/team.html')

@app.route('/ngo/feature.html')
def ngo_feature():
    return render_template('ngo/feature.html')

@app.route('/ngo/testimonial.html')
def ngo_testimonial():
    return render_template('ngo/testimonial.html')

@app.route('/ngo/contact.html')
def ngo_contact():
    return render_template('ngo/contact.html')

# Online Store WebApp routes
@app.route('/store/')
def store_home():
    return render_template('store/index.html')

@app.route('/store/shop.html')
def store_shop():
    return render_template('store/shop.html')

@app.route('/store/cart.html')
def store_cart():
    return render_template('store/cart.html')

@app.route('/store/checkout.html')
def store_checkout():
    return render_template('store/checkout.html')

@app.route('/store/contact.html')
def store_contact():
    return render_template('store/contact.html')

# Portfolio WebApp routes
@app.route('/portfolio/')
def portfolio_home():
    return render_template('portfolio/index.html')

# Restaurant WebApp routes
@app.route('/restaurant/')
def restaurant_home():
    return render_template('restaurant/index.html')

# School WebApp routes
@app.route('/school/')
def school_home():
    return render_template('school/index.html')

@app.route('/school/about.html')
def school_about():
    return render_template('school/about.html')

@app.route('/school/appointment.html')
def school_appointment():
    return render_template('school/appointment.html')

@app.route('/school/classes.html')
def school_classes():
    return render_template('school/classes.html')

@app.route('/school/team.html')
def school_team():
    return render_template('school/team.html')

@app.route('/school/call-to-action.html')
def school_call_to_action():
    return render_template('school/call-to-action.html')

@app.route('/school/contact.html')
def school_contact():
    return render_template('school/contact.html')

# Startup WebApp routes
@app.route('/startup/')
def startup_home():
    return render_template('startup/index.html')

@app.route('/startup/about.html')
def startup_about():
    return render_template('startup/about.html')

@app.route('/startup/service.html')
def startup_service():
    return render_template('startup/service.html')

@app.route('/startup/contact.html')
def startup_contact():
    return render_template('startup/contact.html')

# Travel WebApp routes
@app.route('/travel/')
def travel_home():
    return render_template('travel/index.html')

@app.route('/travel/about.html')
def travel_about():
    return render_template('travel/about.html')

@app.route('/travel/blog.html')
def travel_blog():
    return render_template('travel/blog.html')

@app.route('/travel/services.html')
def travel_services():
    return render_template('travel/services.html')

@app.route('/travel/contact.html')
def travel_contact():
    return render_template('travel/contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)