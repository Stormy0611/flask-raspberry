#import Paramiters to be used
import RPi.GPIO as GPIO
import time

Buzzer = 17

#set GPIO ports to GPIO mapped numbers and not pin number
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set GPIO pins to outputs
GPIO.setup(25, GPIO.OUT)
GPIO.setup(Buzzer, GPIO.OUT)

#Script
 
GPIO.output(25, GPIO.HIGH)
GPIO_Status = GPIO.input(25) #Save current state of port
print(GPIO_Status,file=open("/home/pi/savvyvan/GPIOStats/GPIO25.txt", "w"))

#Audiable alert
GPIO.output(Buzzer,GPIO.HIGH)
time.sleep(0.3)
GPIO.output(Buzzer,GPIO.LOW)
time.sleep(0.5)
GPIO.output(Buzzer,GPIO.HIGH)
time.sleep(0.3)
GPIO.output(Buzzer,GPIO.LOW)
time.sleep(0.5)
GPIO.output(Buzzer,GPIO.HIGH)
time.sleep(0.3)
GPIO.output(Buzzer,GPIO.LOW)

#Announce
print("LOW VOLTAGE!!! Your connected appliances have been shut off to avoid battery damage.",file=open("../notification.txt", "w"))
time.sleep(60)
print("",file=open("../notification.txt", "w"))



