from flask import Flask, request
app = Flask(__name__)

@app.route('/greet')
def greet_person():
    name = request.values.get('text')
    return f'hi {name}!'

@app.route('/')
def hello_world():
    return('Hello, World!')

if __name__ == '__main__':
    app.run()
