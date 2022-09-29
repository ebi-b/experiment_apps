#!/usr/bin/env python3.3
import time
import serial
import sys

text = sys.argv[1]

ser = serial.Serial('/dev/ttyACM0', 3000000, timeout=1, writeTimeout=None)
# start screen transmission
ser.write(('{"screen_string":"' + text +'"}').encode('ascii'))

ser.close()
