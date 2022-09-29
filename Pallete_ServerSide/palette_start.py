#!/usr/bin/python
import time
import serial

ser = serial.Serial('COM4', 1152000)

ser.write('{"start":0}'.encode())
print (ser.readline())
