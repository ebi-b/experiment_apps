#!/usr/bin/env python3.3
import time
import serial
import sys

num = sys.argv[1]

ser = serial.Serial('/dev/ttyACM0', 3000000, timeout=1, writeTimeout=None)
# start screen transmission

# for x in range(0,10):
#   ser.write(('{"screen_display":' + str(x % 8) +'}').encode('ascii'))
#   time.sleep(1)
ser.write(('{"timeout":' + num +'}').encode('ascii'))
ser.close()
