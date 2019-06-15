from alarm import Alarm

path = 'SmartAlarm-01b89ee73267.json'
my_alarm = Alarm(path=path)
my_alarm.take_a_picture()
my_alarm.find_people_in_feed()
