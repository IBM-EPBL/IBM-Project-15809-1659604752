Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@sureshanmugam 
IBM-EPBL
/
IBM-Project-51764-1660983170
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
IBM-Project-51764-1660983170/M.Vinay/Assignment1/ASSIGNMENT 3/ASSIGNMENT 3.py /
@12Preethika
12Preethika Add files via upload
Latest commit a2076be on Oct 10
 History
 1 contributor
42 lines (38 sloc)  888 Bytes

# Blinking LED

import RPi.GPIO as GPIO
from time import sleep 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

while True: 
 GPIO.output(8, GPIO.HIGH) 
 sleep(1) 
 GPIO.output(8, GPIO.LOW)
 sleep(1)
  
# Traffic light Simulation
import RPi.GPIO as GPIO
import time
import signal
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
while True: 
    # Red 
    GPIO.output(9, True) 
    time.sleep(3)  
    # Red and amber 
    GPIO.output(10, True) 
    time.sleep(1)  
    # Green 
    GPIO.output(9, False) 
    GPIO.output(10, False) 
    GPIO.output(11, True) 
    time.sleep(5)  
    # Amber 
    GPIO.output(11, False) 
    GPIO.output(10, True) 
    time.sleep(2)  
    # Amber off (red comes on at top of loop) 
    GPIO.output(10, False)
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
IBM-Project-51764-1660983170/ASSIGNMENT 3.py at main · IBM-EPBL/IBM-Project-51764-1660983170