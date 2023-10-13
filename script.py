#!/usr/bin/env python3
import argparse
import re
import smtplib
from email.mime.text import MIMEText

parser = argparse.ArgumentParser()
parser.add_argument("-e","--email", help="email")
parser.add_argument("-t","--title", nargs='*', help="the title")
parser.add_argument("-m","--message", nargs='*', help="the message")
args = parser.parse_args()

 

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
 
def check(email):
    answer = True
    if(re.fullmatch(regex, email)):
        print("Valid Email")
 
    else:
        print("Invalid Email")
        answer = False
    return answer
checking = check(args.email)
if not checking:
    exit()


subject = args.title
body = args.message
sender = "dvo2014dd@gmail.com"
with open("app.txt", "r") as f:
    password = f.readline().strip()
recipient = args.email

def send_email(subject, body, sender, recipient, password):
    msg = MIMEText(' '.join(body))
    msg['Subject'] = ' '.join(subject)
    msg['From'] = sender
    msg['To'] = recipient
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipient, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipient, password)
