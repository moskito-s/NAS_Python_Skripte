import RPi.GPIO as GPIO
import time
from threading import Timer

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

state = True

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)



def blinkTimerFunc():
        GPIO.output(21,state)
        state = not state
        print("foo")

blinkTimer = RepeatTimer(1, blinkTimerFunc)
blinkTimer.start()

def main():
        while(True):
                pass

if __name__ == "__main__":
    main()

