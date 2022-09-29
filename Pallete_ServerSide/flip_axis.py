#!/usr/bin/python
import time
import serial

ser = serial.Serial('/dev/ttyACM0', 1152000)

ser.write('{"flip":[{"i":7, "m": 1}]}')
print(ser.flushInput())
