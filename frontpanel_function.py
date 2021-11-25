import RPi.GPIO as GPIO
import os
import time
import psutil
from threading import Timer


pin_sw2 = 26
pin_d3 = 19
pin_d1 = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_d3, GPIO.OUT)
GPIO.setup(pin_d1, GPIO.OUT)
GPIO.setup(pin_sw2, GPIO.IN)



class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

obj_Disk_old = psutil.disk_usage('/media/USBdrive/ncdata')
obj_Disk_new = psutil.disk_usage('/media/USBdrive/ncdata')

def buttonPress(channel):
    global buttonStatus
    global obj_Disk_new, obj_Disk_old, pin_d1, pin_d3, pin_d1
    start_time = time.time()

    while GPIO.input(channel) == 0: # Wait for the button up
        pass

    buttonTime = time.time() - start_time    # How long was the button down?

    if .1 <= buttonTime < 2:
        print("reboot")       
        os.system('sudo reboot')         
    elif 2 <= buttonTime :
        print("shutdown")
        GPIO.output(pin_d1,False)
        time.sleep(0.4)
        GPIO.output(pin_d1,True)
        time.sleep(0.4)          
        os.system('sudo shutdown now') 

def checkForHDDChange():
    global obj_Disk_new, obj_Disk_old, pin_d1, pin_d3, pin_d1

    obj_Disk_new = psutil.disk_usage('/media/USBdrive/ncdata')


    if obj_Disk_new.used != obj_Disk_old.used :
        print("HDD changed")
        GPIO.output(pin_d3,True)
        time.sleep(0.4)
        GPIO.output(pin_d3,False)
        time.sleep(0.4)
        obj_Disk_old = obj_Disk_new




GPIO.output(pin_d1,True) #turn on main power light and pull up for switch
GPIO.add_event_detect(pin_sw2, GPIO.FALLING, callback=buttonPress, bouncetime=500)





def main():
    global obj_Disk_new, obj_Disk_old, pin_d1, pin_d3, pin_d1
    print("Frontpanel aktiv")
    hddCheckTimer = RepeatTimer(1, checkForHDDChange)
    hddCheckTimer.start()


    while(True):
        pass

if __name__ == "__main__":
    main()


            