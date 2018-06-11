from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    print dict(request.form)
    payload = dict(request.form)
    first_name = payload['first_name'][0]
    middle_name = payload['middle_name'][0]
    last_name = payload['last_name'][0]
    date_of_birth = payload['date_of_birth'][0]
    address = payload['address'][0]
    hobby = payload['hobby'][0]
    print first_name, middle_name, last_name, date_of_birth, address, hobby
    return render_template('submitted.html', first_name=first_name,
                           middle_name=middle_name, last_name=last_name,
                           date_of_birth=date_of_birth, address=address,
                           hobby=hobby)


@app.route('/sw.js', methods=['GET'])
def sw():
    return app.send_static_file('sw.js')


app.run(debug=True)