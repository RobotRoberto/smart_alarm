from flask import Flask, request, render_template, redirect, url_for 
from models import get_user_cron_tabs, add_user_cron, remove_user_cron

app = Flask(__name__)
weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

def __init__(self):
    app.static_folder = 'static'


@app.route('/', methods=['POST', 'GET'])
def home():
    data = {'title': 'home',
            'crons': get_user_cron_tabs()}
    return render_template('home.html', **data)


@app.route('/add_new_alarm', methods=['POST', 'GET'])
def add_new_alarm():
    data = {'title': 'add a new alarm'}

    if request.method == 'POST':
        alarm_time = request.form.get('time')
        
        if not alarm_time:
            return "Please return a response with alarm time."
        
        alarm_on_days = []

        for weekday in weekdays:
            alarm_on = request.form.get(weekday)
            if alarm_on:
                alarm_on_days.append(weekday)

        if len(alarm_on_days) == 0:
            return "Please input a valid day(s) to have the alarm on."

        add_user_cron(alarm_on_days, alarm_time)
        return redirect(url_for('home'))
        
    else:
        return render_template('add_new_alarm.html', **data)

@app.route('/remove_alarm', methods=['POST'])
def remove_alarm():
    comment = request.form.get("comment")

    if not comment:
        return redirect(url_for('home'))

    remove_user_cron(comment)
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Local ip address is the ip address of your Raspberry Pi, use nmap 
    # in the bash terminal on your pi to figure out
    local_ip = '192.168.1.142' 
    app.run(debug=True, port=5000, host=local_ip)

