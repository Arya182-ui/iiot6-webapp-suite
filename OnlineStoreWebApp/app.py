from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shop.html')
def shop():
    return render_template('shop.html')

@app.route('/cart.html')
def cart():
    return render_template('cart.html')

@app.route('/checkout.html')
def checkout():
    return render_template('checkout.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
