#script by iamnewdev

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import threading
from time import time,sleep
from pygame import mixer
from random import *


def main():

   runAlarm()


def alarmTime():
    t1 = '07:30:00'
    t2 = '17:23:50'
    return t2


def runAlarm():
    def alarm():


        threading.Timer(1,alarm).start()
        timenow = datetime.now()
        al1 = str(timenow.strftime("%H:%M:%S"))
        print(al1)
        x = randint(1,6)
        if al1== alarmTime():
            #webbrowser.open(tones(), new=0)
            x = randint(1,6)
            mixer.init()
            mixer.music.load('path/to/song%d.mp3'% x)
            mixer.music.play()
            print('ALARM! ALARM!')
            sleep(180)
            mixer.music.fadeout(7000)
            sleep(7)
            mixer.quit()
            print('Mixer Ended')


        if al1 != alarmTime():
             print("Systems Normal")


    alarm()




if __name__ == "__main__":
    # execute only if run as a script
    main() 
