import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(24, GPIO.OUT)

GPIO.output(24, GPIO.LOW)
        #turns on the main motor pump

time.sleep(30)
        #holds the motor for 30 seconds

GPIO.output(24, GPIO.HIGH)
        #turns off the motor

time.sleep(60)

import Auto

#GPIO.cleanup()
#cleanup() not required
