import smtplib
from time import time,sleep


# me == the sender's email address
# you == the recipient's email address


fromaddr = 'thesushiman12@gmail.com'
toaddrs  =  ['thesushiman12@gmail.com','sushanta1996@gmail.com']
msg = "Sent from Python"



server = smtplib.SMTP('smtp.gmail.com',587)
print("Setting up Server")
server.starttls()
server.login("thesushiman12@gmail.com", "")
print("Logged In Successfully!")
print("Please confirm that you are sending ",msg," to:", toaddrs)
x = input("Y or N ?")
if x == 'Y' or 'y':
    server.sendmail(fromaddr, toaddrs, msg)
    print("Message Sent")
    server.quit()
    input("Email sent.Press any key to exit!")

if x == 'N' or 'n':

    print("Quitting now")
    sleep(3)
