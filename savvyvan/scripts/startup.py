import RPi.GPIO as GPIO
import os
import logging
from datetime import datetime

#now = str(datetime.datetime.now())
logging.basicConfig(filename='/home/pi/logs/debug.log', level=logging.DEBUG)
#logging.info(str(datetime.now()) + " " )

#Remove log files larger than 5GB
file = '/var/log/syslog'
file1 = '/var/log/syslog.1'
file2 = '/var/log/kern.log'
file3 = '/var/log/kern.log.1'
file4 = '/home/pi/logs/debug.log'

if os.path.getsize(file) > 	1073741824:
    logging.error(str(datetime.now()) + " " + file + " is " + str(os.path.getsize(file)) + " removing")
    os.truncate(file, 10)
    logging.warning(str(datetime.now()) + " " + file + " Over 1GB, Removed")
    os.system("sudo reboot")
if os.path.getsize(file1) > 1073741824:
    logging.error(str(datetime.now()) + " " + file1 + " is " + str(os.path.getsize(file1)) + " removing")
    os.truncate(file1, 10)
    logging.warning(str(datetime.now()) + " " + file1 + " Over 1GB, Removed")
    os.system("sudo reboot")
if os.path.getsize(file2) > 1073741824:
    logging.error(str(datetime.now()) + " " + file2 + " is " + str(os.path.getsize(file2)) + " removing")
    os.truncate(file2, 10)
    logging.warning(str(datetime.now()) + " " + file2 + " Over 1GB, Removed")
    os.system("sudo reboot")
if os.path.getsize(file3) > 1073741824:
    logging.error(str(datetime.now()) + " " + file3 + " is " + str(os.path.getsize(file3)) + " removing")
    os.truncate(file3, 10)
    logging.warning(str(datetime.now()) + " " + file3 + " Over 1GB, Removed")
    os.system("sudo reboot")
if os.path.getsize(file4) > 1073741824:
    logging.error(str(datetime.now()) + " " + file4 + " is " + str(os.path.getsize(file4)) + " removing")
    os.truncate(file4, 10)
    logging.warning(str(datetime.now()) + " " + file4 + " Over 1GB, Removed")
    os.system("sudo reboot")

#Standard Config for all Scripts

#now = str(datetime.datetime.now())
logging.basicConfig(filename='/home/pi/logs/debug.log', level=logging.DEBUG)
#logging.info(str(datetime.now()) + " " )
logging.info(str(datetime.now()) + " StartGPIO Running" )
#-----------------------

#import Paramiters to be used


#set GPIO ports to GPIO mapped numbers and not pin number
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set GPIO pins to outputs
GPIO.setup(1, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

#Script
 
GPIO.output(1, GPIO.HIGH)
GPIO_Status = GPIO.input(1) #Save current state of port
print(GPIO_Status,file=open("/home/pi/savvyvan/GPIOStats/GPIO100.txt", "w"))

GPIO.output(7, GPIO.HIGH)
GPIO_Status = GPIO.input(7) #Save current state of port
print(GPIO_Status,file=open("/home/pi/savvyvan/GPIOStats/GPIO7.txt", "w"))

GPIO.output(8, GPIO.HIGH)
GPIO_Status = GPIO.input(8) #Save current state of port
print(GPIO_Status,file=open("/home/pi/savvyvan/GPIOStats/GPIO8.txt", "w"))

GPIO.output(12, GPIO.HIGH)
GPIO_Status = GPIO.input(12) #Save current state of port
print(GPIO_Status,file=open("/home/pi/savvyvan/GPIOStats/GPIO12.txt", "w"))

GPIO.output(16, GPIO.HIGH)
GPIO_Status = GPIO.input(16) #Save current state of port
print(GPIO_Status,file=open("/home/pi/savvyvan/GPIOStats/GPIO16.txt", "w"))

GPIO.output(20, GPIO.HIGH)
GPIO_Status = GPIO.input(20) #Save current state of port
print(GPIO_Status,file=open("/home/pi/savvyvan/GPIOStats/GPIO20.txt", "w"))

GPIO.output(21, GPIO.HIGH)
GPIO_Status = GPIO.input(21) #Save current state of port
print(GPIO_Status,file=open("/home/pi/savvyvan/GPIOStats/GPIO21.txt", "w"))

GPIO.output(25, GPIO.HIGH)
GPIO_Status = GPIO.input(25) #Save current state of port
print(GPIO_Status,file=open("/home/pi/savvyvan/GPIOStats/GPIO25.txt", "w"))



#-------------------------------------------------------------------------------------
#Subscribe registered email address to Product owners
import requests
from requests.structures import CaseInsensitiveDict

#Load saved email address and format
with open('/home/pi/savvyvan/emailadd.txt') as f:
    emailadd = f.read()
emailadd = emailadd.strip()

#Strip before the @ for the name
character = '@'
name = emailadd.split(character, 1)[0]

#Post to form to subscribe to owners updates
url = "http://web.savvyvan.co.uk:9000/api/subscribers"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Authorization"] = "Basic c2ltb246TjAwZGxlc291cA=="

data = '{\"email\":\"' + emailadd +'\",\"name\":\"'+ name +'\",\"status\":\"enabled\",\"lists\":[5]}'

resp = requests.post(url, headers=headers, data=data)

logging.info(str(datetime.now()) + " Subscribe to Owners updates. Response: " + resp.text)