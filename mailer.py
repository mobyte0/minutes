#!/usr/bin/python

'''
CCOWMU Minute Mailer
This simple script is to mail the minutes after each meeting.
Please set the following:
  Minutes path
  Minutes file naming convention
Please set this script to run in cron
  -Recommended: daily at 11pm
'''

import time
import os
import smtplib

timestamp = time.strftime('%Y%m%d', time.localtime())
datestamp = time.strftime('%a, %b %d', time.localtime())

with os.popen('cat /etc/passwd |grep -e "/home" | grep -v "/bin/false" | grep -Eo "[a-z0-9_]+?@[a-z0-9]+\.[a-z]+"') as f:
  emails = f.readlines()
with open("../do_not_contact.txt", 'r') as f:
  dnc = f.readlines()
emails = [email for email in emails if email not in dnc]
# Comment below to use above
with open("../mailing_list.txt", 'r') as f:
  emails = f.readlines()

try:
  with open("%s.txt" % str(timestamp), 'r') as f:
    minutes = f.read()
except:
  # No minutes today
  exit()

message = 'Subject: %s\n\n%s' % ("Minutes for %s" % str(datestamp), minutes)

try:
  smtpObj = smtplib.SMTP('localhost')
  smtpObj.sendmail("minutes@ccowmu.org", emails, message)
except:
  #print("Error: unable to send email")
  pass