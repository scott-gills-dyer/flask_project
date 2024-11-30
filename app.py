from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Initial page greeting"""
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    """Greet the user by name"""
    return f"hello {name}"
@app.route('/f/<celsius>')
def celsius_to_fahrenheit(celsius):
    """Display fahrenheit from given celsius"""
    celsius = float(celsius)
    return f"{convert_celsius_to_fahrenheit(celsius)}"


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


if __name__ == '__main__':
    app.run()
