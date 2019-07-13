from alarm import Alarm
from time import sleep
from lifxlan import LifxLAN
import os


def play_audio(file_name=None):
    if file_name == None:
        return

    audio_cmd_line = "mplayer " 
    cmd_line = audio_cmd_line + file_name
    os.system(cmd_line)


def set_state(bulb=None, state=None):
    if not bulb or not state:
        return

    bulb.set_power(state)

def init_bulb(num_lights=1):
    lifx = LifxLAN(num_lights)
    devices = lifx.get_lights()

    # I have only one Lifx light currently, may change this code in the future
    bulb = devices[0]
    return bulb

if __name__ =='__main__':
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, 'SmartAlarm-01b89ee73267.json')

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

