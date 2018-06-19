from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    payload = request.get_json()
    print payload
    first_name = payload['first_name']
    middle_name = payload['middle_name']
    last_name = payload['last_name']
    date_of_birth = payload['date_of_birth']
    address = payload['address']
    hobby = payload['hobby']
    print first_name, middle_name, last_name, date_of_birth, address, hobby
    return ''

app.run(debug=True)