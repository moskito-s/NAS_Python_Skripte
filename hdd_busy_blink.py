import RPi.GPIO as GPIO
import time
import psutil

import psutil

obj_Disk = psutil.disk_usage('/media/nextCloudMainHDD')

print (obj_Disk.total / (1024.0 ** 3))
print (obj_Disk.used / (1024.0 ** 3))
print (obj_Disk.free / (1024.0 ** 3))
print (obj_Disk.percent)