import os
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


# input of the switch will change the state of the LED
while True:
    if GPIO.input(26):
        os.system('sudo reboot')