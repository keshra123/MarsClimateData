from flask import Flask, render_template

my_awesome_app = Flask(__name__)

@my_awesome_app.route('/')
def index():
    return render_template('index.html')

@my_awesome_app.route('/aboutthisapplication')
def about():
    return render_template('about.html')

@my_awesome_app.route('/temperature')
def temperature():
    return render_template('temperature.html')

@my_awesome_app.route('/pressure')
def pressure():
    return render_template('pressure.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

