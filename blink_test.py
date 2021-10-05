import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

state = True

# endless loop, on/off for 1 second
while True:
        GPIO.output(21,True)
        time.sleep(0,3)
        GPIO.output(21,False)
        time.sleep(0,4)
