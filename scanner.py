#!/bin/python3

import sys
import socket
from datetime import datetime      #importing for timeout and time taken

#defining the target
if len(sys.argv) != 4:
    target = socket.gethostbyname(sys.argv[1]) #translating hostname to ipv4
else :
    print("Invalid amout of arguments.")
    print("Syntax python3 scanner.py <ip> <Start Port> <End Port>")


start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

#Adding a banner
print("-"*70)
print("Scanning Target:",+target)
print("Time started: "+str(datetime.now()))

try:                       #TRY/EXCEPT block

     for port in range(start_port, end_port+1):

         print("Scanning port:",port)
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #address, TCP
         socket.setdefaulttimeout(2)                           #timeout to prevent delay
         result = s.connect_ex((target, port)) 
         if result == 0:
             print("Port {} is open".format(port))
         s.close()

except KeyboardInterrupt:                  #keyboard clicks
    print("\nexiting program.")
    sys.exit

except socket.gaierror:            #address info errOR
    print("Hostname could not be resolved")
    sys.exit

except socket.error:
    print("Couldn't connect to server")
