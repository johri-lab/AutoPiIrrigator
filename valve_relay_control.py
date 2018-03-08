import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = [14,15,18] 
GPIO.setup(pins, GPIO.OUT)

for pin in pins :
	GPIO.output(pin,  GPIO.HIGH)
	time.sleep(x)
	#x depends on sensor module values x value 
	#keeps on increasing until the soil sensor 
	#value increases to an optimal value

 	if (str(pin)="14"):
 		w="Garden"
 	elif (str(pin)="15"):
		w="seed plot"
	else:
		w="outdoors"

	print( "Watering the " + w +" is comleted" )

GPIO.cleanup()
print "Shutdown All relays"