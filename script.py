from alarm import Alarm
import RPi.GPIO as GPIO

if __name__ =='__main__':
    path = 'SmartAlarm-01b89ee73267.json'
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)


    try:
        my_alarm = Alarm(path=path)
        GPIO.output(18, GPIO.HIGH)
        still_in_bed = my_alarm.find_people_in_feed()
        
        if still_in_bed:
            print("GET OUT OF BED RIGHT NOW!")

    except:
        print("Something is wrong during execution.")
    
    finally:
        GPIO.output(18, GPIO.LOW)
        GPIO.cleanup()


