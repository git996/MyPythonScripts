
import sys

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import threading
import webbrowser
import calendar
import requests
import json
from time import time,sleep
import random
import winsound
#import subprocess
#import threading
import pyaudio
from pygame import mixer
import wave
import mmap
import urllib3
#import cgitb
from bs4 import BeautifulSoup
from random import *
from lxml import html  




def main():

    response = requests.get('https://www.facebook.com/') ## replace with the website you want
   
    parsed_body = html.fromstring(response.text)
    

# Grab links to all images
    images = parsed_body.xpath('//img/@src')  
    print(images)
    input()
    if not images:  
        sys.exit("Found No Images")

# Convert any relative urls to absolute urls
    # Convert any relative urls to absolute urls
    
     
    print ('Found %s images' % len(images))

# Only download first x 10
    for url in images[0:10]:## 100 will scrape 100 pictures

        r = requests.get(url)
        soup = BeautifulSoup(r.content,'html') 
        links = soup.findAll("img")
        f = open('C:/Users/New/Music/im' % url.split('/')[-1], 'w') ## add the folder name
        
        f.write(links.content)
        f.close()

    
   
   #upTime()
  # webData()
   #dateTime()



   
   #realTimejson()
   #matrix()
   #webbrowser.open(url0, new=0) 
   #urll()#runAlarm()
    
   
  
   #soup = BeautifulSoup(data,"html.parser")
   #title = soup.h1.string
   #if title == "HI!" :

       #print (title) 
       #matrix(tones())
       
  








    

def music():
    x = randint(1,229)
    mixer.init()
    print()
    mixer.music.load('C:/Users/New/Music/iMusic/song%d.mp3'% x)
   
    print("Song Started")
    mixer.music.play()
                    

def alarmTime():
    t1 = '06:30:00'
    t2 = '17:58:30'
    return t2
   

def urll():
    urldata = "https://musicplayer119.herokuapp.com/index1.txt"
    now = datetime.now()
    urll.EqWebUrl = requests.get(urldata)
    urll.data  = urll.EqWebUrl.text
      
    
    if urll.EqWebUrl.status_code == 200: 
        print("Connected to Remote!")
    print(urll.data)

    if urll.EqWebUrl.status_code != 200: 
        print("Bad Connection!")
    
 
    if urll.data == 'Com':
       # music()\
        #winsound.Beep(600,5000) 
        #winsound.Beep(200,1000)
        #os.system('newPY.py')
        #print('newPY.py')            
        music()
   
    if urll.data == 'Stop':
        mixer.quit()
        print("Song Stopped")
    if urll.data == 'Play':
        print("Song Playing")
        print(now)

        

    sleep(2)
    urll()
   
               
     
     
        
       
           
    
            
        

      
   # if  urll.data == 'Stop':    
       # sys.exit()
    #if  urll.data == 'Stop':    
      #  mixer.stop()  
    #return urll.data


 
    

#file operations
def filesWrite():
    f = open("textfile.txt","w+")
    for i in range (200):
        f.write("This is line %d\r\n" %(i+1))
    f.close()
 
def filesAppend():
    f = open("textfile.txt","a+")
    for i in range (200):
        f.write("This is line %d\r Append1\n" %(i+1))


def filesRead():
    f = open("textfile.txt","r")
    if f.mode == 'r':
       # content = f.read()
       # print(content)
       fl = f.readline()
       for x in fl:
         print (x)
           
           
 
#dateoperations
def dateTime():
    today = date.today()
    Aprilfools = date(today.year,4,1)

    if Aprilfools < today:
        print("April fools days has already passed. It was %d days ago"  % (today-Aprilfools).days)
        Aprilfools = Aprilfools.replace(year = today.year+1)
        print("It will be april fools in %d days again" % (Aprilfools - today).days)


#internet Data with http requests
def webData():
    file1 = 'let_me_out.wav'
    file2 = 'Holiday.wav'
    webUrl = requests.get("https://git996.github.io/timeline/", "C:/Users/New/Music/Abc.html")
    if webUrl.status_code == 200:
         data  = webUrl.text
         #print(data)
         f = open("webCopy.html","w+")
         
         print("Site Cloned Succesfully")
         
         matrix(file2)

    
    #realtime data
def realTimejson():
    urldata = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    EqWebUrl = requests.get(urldata)
  
    if EqWebUrl.status_code == 200:
        print("Connection Successful...")
        data = EqWebUrl.json()
        if "title" in data["metadata"]:
            print (data["metadata"]["title"])

            #how many events
        count = data["metadata"]["count"] 
        print(str(count) + " earthquakes recorded")

        #locations
        print("-------------------------------------------------")
        for i in data["features"]:
           if i["properties"]["mag"] > 5.0:
               print("Magnitude "+str(i["properties"]["mag"])+" "+i["properties"]["place"])
               print("Tsumani: "+ str(i["properties"]["tsunami"]))
               print("Cooordinates: "+str(i["geometry"]["coordinates"]))
               time = datetime.fromtimestamp((i["properties"]["time"])/1000.0)
               print(time)
               print("-------------------------------------------------")
               f = open("earthquake.json","a+")
               f.write(i["properties"]["place"] +", "+ str(i["geometry"]["coordinates"]) + "\n")
            
        
        winsound.Beep(600,300) 
        winsound.Beep(90,1000)
        file2 = 'Holiday.wav'
        matrix(file2)
        dateTime()
        
        
       


    else: 
        print("Failed to connet to USGS")

def upTime():
    #initialize start datetime
    rn = datetime.now()
     
    
    def calc():
       
        threading.Timer(20.0,calc).start()
        
        #initialize current datetime
        today = datetime.now()
        d = today.strftime("%I:%M %p")
        print("\n"+str(today.hour)+" hours "+str(today.minute)+ " minute "+str(today.second)+" seconds.")
        print(d)
        print("Day: "+str(today.day))
        totalTime = (today-rn).seconds
        print(str(totalTime) + " seconds")
        f = open("upTimelog.txt","a+")
        f.write(today.strftime("%Y/%m/%d")+","+str(totalTime)+"\n")
        print("Written to file..a")      
    
    calc()
    


def matrix(audiofile):

    chunk = 1024
    f = wave.open(audiofile)
    p = pyaudio.PyAudio()
    #open stream  
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
               channels = f.getnchannels(),  
               rate = f.getframerate(),  
               output = True)  
    data = f.readframes(chunk) 
    while data:
        stream.write(data)  
        data = f.readframes(chunk)  
    
    stream.stop_stream()  
    stream.close()  

 
    p.terminate()
if __name__ == "__main__":
    # execute only if run as a script
    main()
   
    
