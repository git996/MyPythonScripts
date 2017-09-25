from bs4 import BeautifulSoup
import requests
from datetime import datetime
from datetime import date
import requests
import smtplib
import schedule
import time





class MyFeed():

    def quotes(self):
        site1 = 'https://www.brainyquote.com/quotes_of_the_day.html'
        r  = requests.get(site1)
        message = []
        print (r.headers['content-type'])
        data = r.text
        soup = BeautifulSoup(data,'lxml')
        print(soup.title.string)
        now = datetime.now()
        for quote in soup.find_all(title = "view quote", limit = 3):
            message.append(quote.string)

        subject = """Subject: Good Morning! Here's today's feed!
        """

        self.send_mail('thesushiman12@gmail.com',subject, message)

    def send_mail(self,toaddrs,sub,msg):
        mg1 = sub + '\n' + msg[0] + '\n' + msg[2]
        fromaddr = 'pysauce@gmail.com'
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login("pysauce@gmail.com", "mailbotyoungdaisy")
        server.sendmail(fromaddr, toaddrs, mg1)
        server.quit()
        print("Message Sent")



def main():
    feed =  MyFeed()
    schedule.every().day.at("16:26").do(feed.quotes)
    while True:
        schedule.run_pending()
        time.sleep(1)







if __name__ == "__main__":
    # execute only if run as a script
    main()
