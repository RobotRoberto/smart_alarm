from crontab import CronTab, CronItem

command_str = '/home/pi/.virtualenvs/smart_alarm/bin/python3.5 /home/pi/projects/smart_alarm/script.py >> /home/pi/out.txt 2>&1'

def _get_hour_minute(alarm_time: str):
    ## gets the index of ':' for minute and hour for schedule
    index = alarm_time.find(':')
    hour = alarm_time[index + 1:]
    minute = alarm_time[:index]
    return int(hour), int(minute)


def _get_alarm_times(item : CronItem) -> str:
    return str(item.dow) + " " + str(item.hour) + " " + str(item.minute)


def get_user_cron_tabs():
    user_cron = CronTab(user=True)
    return [job.comment for job in user_cron]

def add_user_cron(days_on: list, alarm_time: str) -> None:
    """
    This function adds a new crontab for the alarm with schedule on
    days in the list days_on. For example, ["Mon", "Thu"] means the
    alarm script will run during Monday and Thursday. The alarm_time
    is the time when the script will run
    """

    ## creates new crontab with alarm script command
    user_cron = CronTab(user=True)
    job = user_cron.new(command = command_str)
    
    ## setting the schedule
    hour_val, minute_val = _get_hour_minute(alarm_time)
    job.minute.on(hour_val)
    job.hour.on(minute_val)
    
    ## setting the days of schedule
    days_on = [day.upper() for day in days_on]
    job.dow.on(*days_on)
    
    ## setting comment to use for display and delete id later
    job.comment = str(job.dow) + " " + alarm_time

    user_cron.write_to_user(user=True)


def remove_user_cron(comment_str: str):
    """
    This function removes crontabs for the alarm with the comment
    of this comment string passed in
    """

    ## gets the crontab
    user_cron = CronTab(user=True)
    user_cron.remove_all(comment=comment_str)
    user_cron.write_to_user(user=True)


if __name__ == '__main__':
    add_user_cron(['mon', 'tue'], "12:00")
