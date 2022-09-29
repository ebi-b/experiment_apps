#!/usr/bin/python
import time
import serial

ser = serial.Serial('COM4', 1152000)
x= ser.flushInput()
print(x)
ser.write('{"midimap":[{"i":1, "s":[{"c":0, "mc":7, "t":2, "d":30}]}]}'.encode())
ser.flushOutput()
t=ser.readlines()

print(t)

#time.sleep(50)