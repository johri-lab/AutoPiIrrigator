import os
import time
from datetime import datetime
def sync():
    print("syncing time with RTC")
    time.sleep(.2)
    try:
        os.system('sudo hwclock -w')
        time.sleep(.2)
        print("Synced"),
        #os.system('date')
    except RuntimeError:
        print("Failed to Sync time,Check RTC")
        
    #print(os.system('date;sudo hwclock -r'))

def currenttime():
    t=str(datetime.now().time())
    return t[:8]
def currentdate():
    return str(datetime.now().date())
