import time
import os
import BME280 as bme
import RTC as rtc
from subprocess import call

def watering_time():
    return time.strftime("%H:%M")

target_time= "16:00"

while True:
       
    if watering_time() == target_time:
        time.sleep(0.1)         
        call(["python", "valve.py"])
