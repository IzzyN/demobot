from flask import Flask, request
app = Flask(__name__)

@app.route('/greet', methods=['GET', 'POST'])
def greet_person():
    name = request.values.get('text')
    return f'hi {name}!'

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return('Hello, World!')

@app.route('/weather', methods=['GET', 'POST'])
def check_weather():
    temp = request.values.get('temp')
    temp = int(temp)
    if temp > 30:
        return "It's so hot!"
    else:
        return(f'The temperature is {temp}')

if __name__ == '__main__':
    app.run(debug=True)
