#!/usr/bin/python
import time
import serial

ser = serial.Serial('/dev/ttyACM0', 1152000)

ser.write('{"hidmap":[{"i":2, "s":[]}]}')
