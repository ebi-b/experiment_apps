#!/usr/bin/python
import time
import serial

ser = serial.Serial('/dev/ttyACM0', 1152000)

ser.write('{"joymap":[{"i":2, "s":[{"c":3, "a":3, "b":0}]}]}')
