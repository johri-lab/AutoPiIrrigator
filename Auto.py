import time
import os
import BME280 as bme
import RTC as rtc

def watering_time():
    return time.strftime("%H:%M")

target_time= "16:00"
#turns on the motor pump at 4 p.m. everyday! 


while True:
    
    if watering_time() == target_time:
        time.sleep(0.1)
        import valve.py

