from flask import Flask, request, render_template


app = Flask(__name__)


def __init__(self):
    app.static_folder = 'static'


@app.route('/add_new_alarm', methods=['POST', 'GET'])
def add_new_alarm():
    data = {'title': 'add a new alarm'}

    if request.method == 'POST':
        alarm_time = request.form['time']
        return alarm_time

    return render_template('home.html', **data)

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
