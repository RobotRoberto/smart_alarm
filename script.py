from alarm import Alarm
import RPi.GPIO as GPIO
from time import sleep
import os

def play_audio(file_name=None):
    if file_name == None:
        return

    audio_cmd_line = "omxplayer " 
    cmd_line = audio_cmd_line + file_name
    os.system(cmd_line)


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
            play_audio(os.getcwd() + "/wake_up_sounds/alarm_sound.mp3")

    except Exception as e:
        print(e)
        print("Something is wrong during execution.")
        play_audio(os.getcwd() + "/wake_up_sounds/error.mp3")

    
    finally:
        GPIO.output(18, GPIO.LOW)
        GPIO.cleanup()


