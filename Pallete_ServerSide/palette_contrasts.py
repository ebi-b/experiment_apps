#!/usr/bin/env python3.3
import time
import serial
import sys
import os

r = int(sys.argv[1])
g = int(sys.argv[2])
b  = int(sys.argv[3])
m = int(sys.argv[4])

ser = serial.Serial('/dev/ttyACM0', 3000000, timeout=1, writeTimeout=None)

# start screen transmission
ser.write(('{"contrast":1}').encode('ascii'))

arr = [r, g, b, m]

# write contrasts
ser.write(bytearray(arr))
ser.close()
