from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/appointment.html')
def appointment():
    return render_template('appointment.html')

@app.route('/classes.html')
def classes():
    return render_template('classes.html')

@app.route('/team.html')
def team():
    return render_template('team.html')

@app.route('/call-to-action.html')
def call_to_action():
    return render_template('call-to-action.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
