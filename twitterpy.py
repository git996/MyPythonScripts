

import tweepy
import json
from datetime import date
import csv
from pygame import mixer
from random import *
import requests
import winsound
from time import sleep
from textblob import TextBlob
from textblob import Word




def main():
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_secret = ''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_secret)
    api =  tweepy.API(auth)

    print("Scanning for tweets..")
    class MyStreamListener(tweepy.StreamListener):

        cnt = 0
        tweet_analysis=''
        tweet=''
        def on_status(self, data):

            self.cnt = self.cnt +1
            x = randint(1, 119)
            user1 = data.user
            time = data.created_at

            #print(user1.screen_name)

            self.tweet = data.text

            tw_data = TextBlob(data.text)
            if tw_data.sentiment.polarity < 0:
                winsound.Beep(300,200)
                print('Negative')
                #print(self.tweet)
                #filesWrite(self.tweet)

            if tw_data.sentiment.polarity > 0:
                winsound.Beep(600,100)
                print('Positive')
                #print(self.tweet)
                #filesWrite(self.tweet)
            if tw_data.sentiment.polarity > 0.5:
                winsound.Beep(200,1000)
                print('Positive-----------')
                filesWrite(self.tweet)
                #print(self.tweet)



            self.tweet_analysis = str(tw_data.sentiment)

            print(self.tweet_analysis)


            #filesWrite(self.tweet_analysis)
            print('----------------------------------------------')
            #winsound.Beep(600,100)
            #winsound.Beep(500,100)
            #winsound.Beep(400,500)
            #comdata = data.text.split()

            #if data.text == 'play' or 'Play':








    #instan the class
    global key
    key = 'missile'
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    myStream.filter(track=[key])






def filesWrite(num):
    f = open("tweets.csv","a+")
    f.write('Tweets with keyword ' +key+ ','+num+'\n')
    f.close()

def music(rand):


    mixer.init()
    #rand = randint(1,119)
    url = 'C:/Users/New/Music/im/iMusic/song (%d).mp3' % rand

    mixer.music.load(url)
    mixer.music.play()
    volume = mixer.music.get_volume()*100

    print("Volume:", volume)








if __name__ == "__main__":
    # execute only if run as a script
    main()
