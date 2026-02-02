from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/service.html')
def service():
    return render_template('service.html')

@app.route('/project.html')
def project():
    return render_template('project.html')

@app.route('/team.html')
def team():
    return render_template('team.html')

@app.route('/feature.html')
def feature():
    return render_template('feature.html')

@app.route('/testimonial.html')
def testimonial():
    return render_template('testimonial.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/404.html')
def error_404():
    return render_template('404.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
