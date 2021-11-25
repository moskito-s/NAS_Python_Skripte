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

obj_Disk_old_size = 0
obj_Disk_new_size = 0


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
    global obj_Disk_old_size, obj_Disk_new_size, pin_d1, pin_d3, pin_d1

    try:

        obj_Disk_new = psutil.disk_usage('/media/USBdrive/ncdataa')
        obj_Disk_new_size = obj_Disk_new.used


    except Exception:
        GPIO.output(pin_d1,False)
        time.sleep(0.2)
        GPIO.output(pin_d1,True)
        print("ERROR: Nextcloud festplatte nicht gefunden")


    if obj_Disk_new_size != obj_Disk_old_size :
        print("HDD changed")
        GPIO.output(pin_d3,True)
        time.sleep(0.4)
        GPIO.output(pin_d3,False)
        obj_Disk_old_size = obj_Disk_new_size




GPIO.add_event_detect(pin_sw2, GPIO.FALLING, callback=buttonPress, bouncetime=500)


def main():
    global obj_Disk_new, obj_Disk_old, pin_d1, pin_d3, pin_d1
    print("Frontpanel aktiv")
    GPIO.output(pin_d1,True) #turn on main power light and pull up for switch
    hddCheckTimer = RepeatTimer(0.8, checkForHDDChange)
    hddCheckTimer.start()


    while(True):
        pass

if __name__ == "__main__":
    main()


            