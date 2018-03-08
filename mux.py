pin=[[0,0,0,0],
     [0,0,0,1],
     [0,0,1,0],
     [0,0,1,1],
     [0,1,0,0],
     [0,1,0,1],
     [0,1,1,0],
     [0,1,1,1],
     [1,0,0,0],
     [1,0,0,1],
     [1,0,1,0],
     [1,0,1,1],
     [1,1,0,0],
     [1,1,0,1],
     [1,1,1,0],
     [1,1,1,1]]
import time
import RPi.GPIO as GPIO
# Use GPIO numbers not pin numbers
GPIO.setmode(GPIO.BCM)
# set up the GPIO channels - one input and one output
GPIO.setup(26, GPIO.IN)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

def select(x):

    GPIO.output(12,pin[int(x)][0])
    GPIO.output(16,pin[int(x)][1])
    GPIO.output(20,pin[int(x)][2])
    GPIO.output(21,pin[int(x)][3])
    print('pin no'),
    print(x),
    print('selected')

def pinvalue(p):
    select(p)
    time.sleep(1)
    y=GPIO.input(26)
    GPIO.cleanup()
    return (y)

