#import Paramiters to be used
import RPi.GPIO as GPIO

#set GPIO ports to GPIO mapped numbers and not pin number
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set GPIO pins to outputs
GPIO.setup(25, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

#Script
 
GPIO.output(25, GPIO.HIGH)
GPIO_Status = GPIO.input(25) #Save current state of port
print(GPIO_Status,file=open("/home/pi/savvyvan/GPIOStats/GPIO25.txt", "w"))
#Tap Noise
GPIO.output(17,GPIO.HIGH)
time.sleep(0.02)
GPIO.output(Buzzer,GPIO.LOW)

