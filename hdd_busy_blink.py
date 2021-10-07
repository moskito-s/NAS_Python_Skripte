import RPi.GPIO as GPIO
import time
import psutil

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

GPIO.output(21,True)
time.sleep(0.4)
GPIO.output(21,False)
time.sleep(0.4)


obj_Disk_old = psutil.disk_usage('/media/nextCloudMainHDD')
obj_Disk_new = psutil.disk_usage('/media/nextCloudMainHDD')


# endless loop, on/off for 1 second
while True:

            
    time.sleep(0.5)

    obj_Disk_new = psutil.disk_usage('/media/nextCloudMainHDD')

    if obj_Disk_new.used != obj_Disk_old.used :
        GPIO.output(21,True)
        time.sleep(0.4)
        GPIO.output(21,False)
        time.sleep(0.4)

    obj_Disk_old = obj_Disk_new
