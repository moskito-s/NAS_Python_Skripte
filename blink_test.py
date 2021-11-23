import RPi.GPIO as GPIO
import time
import threading as th

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

state = True

def blinkTimerFunc():
        GPIO.output(21,state)
        state = not state


def main():
        blinkTimer = RepeatTimer(1, blinkTimerFunc)
        
        while(True):
                pass

if __name__ == "__main__":
    main()

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)