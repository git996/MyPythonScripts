#script by iamnewdev/git996

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import threading
import sys
from time import time,sleep
from pygame import mixer
from random import *


def main():
   runAlarm()


def alarmTime():
    t1 = '07:00:00'
    t2 = '14:14:20'
    return t2


def runAlarm():
    def alarm():
        threading.Timer(1,alarm).start()
        timenow = datetime.now()
        al1 = str(timenow.strftime("%H:%M:%S"))
        print(al1)
        x = randint(1,119)
        if al1== alarmTime():
            #webbrowser.open(tones(), new=0)

            mixer.init()
            mixer.music.load('C:/Users/New/Music/im/iMusic/song (%d).mp3'% x)
            mixer.music.play()
            print('ALARM!')
            sleep(240)
            mixer.music.fadeout(7000)
            sleep(7)
            mixer.quit()
            print('Closing Mixer')

        if al1 != alarmTime():
             print("Systems Normal! Alarm set for: ", alarmTime())

    alarm()



if __name__ == "__main__":
    # execute only if run as a script
    main()
