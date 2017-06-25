import cv2
import sys
import os
import logging as log
import datetime as dt
from time import sleep
import winsound
from pygame import mixer
from datetime import datetime
import webbrowser
import subprocess
from random import *



cascPath = "haarcascade_frontalface_default.xml"
#cascPath= "haarcascades/haarcascade_russian_plate_number.xml"
#cascPath = "parojos.xml"
#cascPath = "HS.xml"


today = datetime.now()
todaystr = today.strftime("%Y%m%d-%H%M%S")
camera_port = 0
ramp_frames = 30
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

video_capture = cv2.VideoCapture(0)
anterior = 0
mixer.init()
mixer.music.load('detected.mp3')

def music():

    mixer.init()
    rand = randint(1,119)
    url = 'C:/Users/New/Music/im/iMusic/song (%d).mp3' % rand

    mixer.music.load(url)
    mixer.music.play()
    volume = mixer.music.get_volume()*100


    print("Volume:", volume)



def tones():

    for i in range(1,10):
        winsound.Beep(700, 700)
        winsound.Beep(900, 800)

    winsound.Beep(100,2000)





while True:

    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )


   #Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (200, 200, 90), 2)

    if  len(faces) > 0:
        url0 ="https://pandora.com"
        url1 = "https://en.wikipedia.org/wiki/Special:Random"
        #tones()

        #print("Object detected")
        #music()
        mixer.music.play()

        #print("\nOpening" + url0)



        #p = subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        #webbrowser.open(url0, new=0)
        webbrowser.open(url1, new=0)
        sleep(1)
        #p.kill()



        #sleep(3)
        #log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))


        for i in range(ramp_frames):
            temp = frame
        print("Taking image...")
      # Take the actual image we want to keep
        camera_capture = frame
        file = "C:/Users/New/Pictures/imagelog11/%s.png" %todaystr
        cv2.imwrite(file, camera_capture)



        sys.exit()

    # Display the resulting frame
    cv2.imshow('Detections', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        sys.exit()



# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
