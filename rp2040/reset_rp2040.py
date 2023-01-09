#!/usr/bin/python3

# Import required Python libraries
import RPi.GPIO as GPIO
import time

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

#disable warnings
GPIO.setwarnings(False)

# init list with pin numbers

pinList = [5]

# loop through pins and set mode and state to 'low'

for i in pinList:
    GPIO.setup(i, GPIO.OUT)

def trigger() :
        for i in pinList:
          GPIO.output(i, GPIO.HIGH)
          time.sleep(0.5)
          GPIO.output(i, GPIO.LOW)
          GPIO.cleanup()

try:
    trigger()

except KeyboardInterrupt:
  print ("  Quit") 
  # Reset GPIO settings
  GPIO.cleanup()
