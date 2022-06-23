
# Enable the below to make this script power off the Raspberry Pi
import os
import time
os.system("truncate -s 0 ../readings/voltage_graph.txt")

print("Voltage graph successfully reset.",file=open("../notification.txt", "w"))
time.sleep(30)
print("",file=open("../notification.txt", "w"))
