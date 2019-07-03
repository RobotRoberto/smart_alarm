from alarm import Alarm
import RPi.GPIO as GPIO
from time import sleep
import os

if __name__ =='__main__':
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, 'SmartAlarm-01b89ee73267.json')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)


    try:
        my_alarm = Alarm(path=path)
        GPIO.output(18, GPIO.HIGH)
        sleep(2)
        my_alarm.take_a_picture()
        still_in_bed = my_alarm.find_people_in_feed()
        
        if still_in_bed:
            print("GET OUT OF BED RIGHT NOW!")

    except Exception as e:
        print(e)
        print("Something is wrong during execution.")
    
    finally:
        GPIO.output(18, GPIO.LOW)
        GPIO.cleanup()


