#!/usr/bin/env python3.3
import time
import serial
import sys

num = sys.argv[1]

ser = serial.Serial('/dev/ttyACM0', 3000000, timeout=1, writeTimeout=None)

# toggle screen timing out
ser.write(('{"timeout":' + num +'}').encode('ascii'))
ser.close()
