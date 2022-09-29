#!/usr/bin/python
import time
import serial
import sys

ser = serial.Serial('COM5', 3000000, timeout=1, writeTimeout=None)
# start screen transmission
ser.write(('{"screen_ready": 1}').encode('ascii'))
#print(ser.readlines())
resp = ser.read(24)
print(resp)
if "0" in resp:
  print("fail")
elif "1" in resp:
  print("pass")

ser.close()
