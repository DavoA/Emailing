#!/usr/bin/env python3
"""
    These are imported modules.
"""
import argparse
import re
import sys
import os
import smtplib
from email.mime.text import MIMEText

def check_file_existence(fname):
    """
        This is created to check file exestence.
    """
    answer = True
    if not os.path.isfile(fname):
        print(f"Input file does not exists. Please check {fname}")
        answer = False
    return answer

def get_code(fname):
    """
        This is created to get code from txt file.
    """
    with open(fname,"r", encoding="utf-8") as mfile:
        return mfile.readline().strip()

def check(email):
    """
        This is created to check email validation.
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    answer = True
    try:
        if not re.fullmatch(regex, email):
            print("Invalid Email")
            answer = False
    except TypeError:
        print("You must enter the email in correct way. Check the argparse help using -h")
        answer = False
    return answer

def send_email(subject, body, sender, recipient, password):
    """
        This is created to send the message.
    """
    try:
        msg = MIMEText(' '.join(body))
        msg['Subject'] = ' '.join(subject)
        msg['From'] = sender
        msg['To'] = recipient
    except TypeError:
        print("You must enter the message in correct way. Check the argparse help using -h")
        sys.exit()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        try:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipient, msg.as_string())
        except smtplib.SMTPAuthenticationError:
            print("Something wrong with the email and password. Please check! ")
            sys.exit()
    print("Message sent!")

def main():
    """
        This is the main.
    """
    fname = "app.txt"
    checking_file = check_file_existence(fname)
    if not checking_file:
        print("Check your file existence!")
        sys.exit()
    parser = argparse.ArgumentParser()
    parser.add_argument("-e","--email", help="email")
    parser.add_argument("-t","--title", nargs='*', help="the title")
    parser.add_argument("-m","--message", nargs='*', help="the message")
    args = parser.parse_args()
    checking_email = check(args.email)
    if not checking_email:
        sys.exit()
    subject = args.title
    body = args.message
    sender = "dvo2014dd@gmail.com"
    password = get_code(fname)
    recipient = args.email
    send_email(subject, body, sender, recipient, password)

main()
