from alarm import Alarm
from time import sleep
from lifxlan import LifxLAN
import os


def play_audio(file_name=None):
    """
    Plays the audio file given the file path name
    """
    if file_name == None:
        return

    audio_cmd_line = "mplayer " 
    cmd_line = audio_cmd_line + file_name
    os.system(cmd_line)


def set_state(bulb=None, state=None):
    """
    Sets the state of the Lifx bulb 
    """
    if not bulb or not state:
        return

    bulb.set_power(state)

def init_bulb(num_lights=1):
    """
    Initializes the light bulb for use
    """
    lifx = LifxLAN(num_lights)
    devices = lifx.get_lights()

    # I have only one Lifx light currently, may change this code in the future
    bulb = devices[0]
    return bulb

if __name__ =='__main__':
    """
    The main script for running the alarm, initializes the bulb and searches
    for people in the picture taken and uploaded to Google Vision API.
    If API finds a person in the picture, then the script will play the alarm
    sound. Then, the script will run again in 30 seconds to re-evaluate if
    the person is still in bed.
    """
    dirname = os.path.dirname(__file__)

    # If you are using this application for yourself, then update the API_KEY
    # with your own path
    API_KEY = 'SmartAlarm-01b89ee73267.json'
    path = os.path.join(dirname, API_KEY)
    
    try:
        bulb = init_bulb()
        set_state(bulb, "on")
        my_alarm = Alarm(path=path)
        still_in_bed = True
        while still_in_bed:
            still_in_bed = my_alarm.find_people_in_feed()
        
            if still_in_bed:
                print("GET OUT OF BED RIGHT NOW!")
                play_audio(os.getcwd() + "/wake_up_sounds/alarm_sound.mp3")
                sleep(30)

    except Exception as e:
        print(e)
        print("Something is wrong during execution.")
        play_audio(os.getcwd() + "/wake_up_sounds/error.mp3")

    
    finally:
        set_state(bulb, "off")
        print("Script finished")

