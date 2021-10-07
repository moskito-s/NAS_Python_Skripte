import RPi.GPIO as GPIO
import time
import psutil

import psutil

obj_Disk = psutil.disk_usage('/media/nextCloudMainHDD')

print (obj_Disk.total)
print (obj_Disk.used)
print (obj_Disk.free)
print (obj_Disk.percent)