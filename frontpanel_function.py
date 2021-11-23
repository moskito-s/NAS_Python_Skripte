import RPi.GPIO as GPIO
import os
import time
import psutil
from threading import Timer

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(26,GPIO.IN)

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

obj_Disk_old = psutil.disk_usage('/media/USBdrive/ncdata')
obj_Disk_new = psutil.disk_usage('/media/USBdrive/ncdata')

def buttonPress(channel):
    global buttonStatus
    start_time = time.time()

    while GPIO.input(channel) == 0: # Wait for the button up
        pass

    buttonTime = time.time() - start_time    # How long was the button down?

    if .1 <= buttonTime < 2:
        print("reboot")       
        os.system('sudo reboot')         
    elif 2 <= buttonTime :
        print("shutdown")
        GPIO.output(21,False)
        time.sleep(0.4)
        GPIO.output(21,True)
        time.sleep(0.4)          
        os.system('sudo shutdown now') 

def checkForHDDChange():
    global obj_Disk_new, obj_Disk_old

    GPIO.output(21,True)
    time.sleep(0.4)
    GPIO.output(21,False)
    time.sleep(0.4)

    if obj_Disk_new.used != obj_Disk_old.used :
        GPIO.output(21,True)
        time.sleep(0.4)
        GPIO.output(21,False)
        time.sleep(0.4)

    obj_Disk_old = obj_Disk_new


GPIO.output(20,True) #turn on main power light and pull up for switch
GPIO.add_event_detect(26, GPIO.FALLING, callback=buttonPress, bouncetime=500)





def main():
    print("Frontpanel aktiv")
    hddCheckTimer = RepeatTimer(1, checkForHDDChange)
    hddCheckTimer.start()


    while(True):
        pass

if __name__ == "__main__":
    main()


            