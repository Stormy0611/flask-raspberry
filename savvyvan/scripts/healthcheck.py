#Standard Config for all Scripts
import logging
from datetime import datetime
#now = str(datetime.datetime.now())
logging.basicConfig(filename='/home/pi/logs/debug.log', level=logging.DEBUG)
#logging.info(str(datetime.now()) + " " )
#-----------------------


import urllib.request
import subprocess
import os
from socket import timeout
import time 

host = "http://www.google.co.uk"
host1 = "http://www.savvyvan.co.uk"
status = True
timeout = 10
brcmfmac = False

def removelogs():
    #Remove log files larger than 5GB
    file = '/var/log/syslog'
    file1 = '/var/log/syslog.1'
    file2 = '/var/log/kern.log'
    file3 = '/var/log/kern.log.1'

    if os.path.getsize(file) > 	1073741824:
        logging.error(str(datetime.now()) + " " + file + " is " + str(os.path.getsize(file)) + " removing")
        os.truncate(file, 10)
        logging.warning(str(datetime.now()) + " " + file + " Over 1GB, Removed")
    if os.path.getsize(file1) > 1073741824:
        logging.error(str(datetime.now()) + " " + file1 + " is " + str(os.path.getsize(file1)) + " removing")
        os.truncate(file1, 10)
        logging.warning(str(datetime.now()) + " " + file1 + " Over 1GB, Removed")
    if os.path.getsize(file2) > 1073741824:
        logging.error(str(datetime.now()) + " " + file2 + " is " + str(os.path.getsize(file2)) + " removing")
        os.truncate(file2, 10)
        logging.warning(str(datetime.now()) + " " + file2 + " Over 1GB, Removed")
    if os.path.getsize(file3) > 1073741824:
        logging.error(str(datetime.now()) + " " + file3 + " is " + str(os.path.getsize(file3)) + " removing")
        os.truncate(file3, 10)
        logging.warning(str(datetime.now()) + " " + file3 + " Over 1GB, Removed")

def restartwlan0():
    os.system("sudo /usr/sbin/rmmod brcmfmac")
    os.system("sudo /usr/sbin/modprobe brcmfmac roamoff=1")
    logging.warning(str(datetime.now()) + " Restarted WLAN")
    
    print("WLAN reset",file=open("../notification.txt", "w"))
    time.sleep(30)
    print("",file=open("../notification.txt", "w"))


#Check Internet connection.
def connect():
    try:
        urllib.request.urlopen(host, timeout=timeout)
        return True
    except:
        return False

def search_str(file_path, word):
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:
            return True #brcmfmac in error 
        else:
            return False #brcmfmac ok

status = connect()
if status==True:
    wifi = "up"
    logging.info(str(datetime.now()) + ' WLAN is UP')
else:
    def connect():
        try:
            urllib.request.urlopen(host1, timeout=timeout)
            return True
        except:
            return False
    
    #Return result to wifi
    status = connect()
    if status==True :
        wifi = "up"
        logging.info(str(datetime.now()) + ' WLAN is UP')
    else:
        wifi = "down"
        logging.warning(str(datetime.now()) + ' WLAN is Down')

        brcmfmac = search_str(r'/var/log/kern.log', 'brcmfmac: brcmf_sdio_htclk: HT Avail request error: -5')
        
        if brcmfmac==True :
            logging.error(str(datetime.now()) + ' brcmfmac in error')
            restartwlan0()
            removelogs()
        else:
            logging.info(str(datetime.now()) + ' brcmfmac ok, WIFI not connected')
            removelogs()


        
