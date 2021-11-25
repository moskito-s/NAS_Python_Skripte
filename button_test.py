import RPi.GPIO as GPIO
import time
import psutil

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)
GPIO.setup(20, GPIO.OUT)

GPIO.setup(26, GPIO.OUT)


def buttonPress(channel):
    global buttonStatus
    start_time = time.time()

    while GPIO.input(channel) == 0: # Wait for the button up
        pass

    buttonTime = time.time() - start_time    # How long was the button down?

    if .1 <= buttonTime < 2:        # Ignore noise
        buttonStatus = 1        # 1= brief push

    elif 2 <= buttonTime < 4:         
        buttonStatus = 2        # 2= Long push


    print(buttonStatus)


GPIO.add_event_detect(26, GPIO.FALLING, callback=buttonPress, bouncetime=500)

def main():
    print("Button Check")
    GPIO.output(20,True)#pullup
    while(True):
        pass

if __name__ == "__main__":
    main()


            

