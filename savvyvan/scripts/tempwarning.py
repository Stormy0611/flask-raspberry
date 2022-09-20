#Standard Config for all Scripts
import logging
from datetime import datetime
#now = str(datetime.datetime.now())
logging.basicConfig(filename='/home/pi/logs/debug.log', level=logging.DEBUG)
#logging.info(str(datetime.now()) + " " )
logging.info(str(datetime.now()) + " Temperature Service Started " )
#-----------------------

import subprocess
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import base64
import time
import RPi.GPIO as GPIO

Buzzer = 17
GPIO.setwarnings(False)
GPIO.cleanup()			#clean up at the end of your script
GPIO.setmode(GPIO.BCM)		#to specify whilch pin numbering system
GPIO.setup(Buzzer, GPIO.OUT)

def main():
    while True:
        #Get temperature reading
        cmd="vcgencmd measure_temp"
        output = str(subprocess.check_output(cmd, shell=True))
        num = re.findall('\d+\.\d+', output) 
        temp = float(num[0])
        print("Device Temperature " + str(temp) + "\'C")
                
        if temp > 80:
                logging.warning(str(datetime.now()) + " System Temperture" + str(temp) )
                #read email address
                with open('/home/pi/savvyvan/emailadd.txt') as f:
                        receiver = f.read()
                sender = "notifications@savvyvan.co.uk"
                print(receiver)

                #send email notification
                msg = MIMEText('Dear User\n\nSavvyVan temperature is high ' + str(temp) + '\'C.\n\nPlease take action to reduce the temperature or turn off the device to prevent damage to your device.\n\nThankyou\n\nSavvyVan\nSupport@SavvyVan.co.uk\nhttps://www.savvyvan.co.uk\n\n\nPlease do not reply, this mailbox is unmonitored')

                msg['Subject'] = 'High Temperature Alert! ' + str(temp) + '\'C'
                msg['From'] = formataddr((str(Header('SavvyVan Notifications', 'utf-8')), sender))
                msg['To'] = receiver
                msg['X-Priority'] = '2'

                user = 'outbound@ripsolutions.co.uk'
                password = (base64.b64decode("c2FjbXUwLUdvbWh1ay14YXF0YXA=").decode("utf-8"))

                with smtplib.SMTP("smtp.ionos.co.uk", 25) as server:

                    server.login(user, password)
                    server.sendmail(sender, receiver, msg.as_string())
                    print('Mail Sent - High Temperture Alert! ' + str(temp) + '\'C')
                logging.info(str(datetime.now()) + ' Mail Sent - High Temperture Alert! ' + str(Voltage_graph_round) + 'v. Mail Sent to ' + str(receiver) )

                #Audible Alert
                GPIO.output(Buzzer,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(Buzzer,GPIO.LOW)


                #Display message onscreen
                print("Device High Temperature Alert! " + str(temp) + "\'C. Please take action or shutdown to prevent damage.",file=open("/home/pi/savvyvan/notification.txt", "w"))
                time.sleep(30)
                print("",file=open("/home/pi/savvyvan/notification.txt", "w"))
        
        time.sleep(1800)

        
if __name__ =='__main__':
    try:
            main()
            pass
    except KeyboardInterrupt:
            pass

GPIO.cleanup()