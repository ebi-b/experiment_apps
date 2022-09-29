#!/usr/bin/python
import time
import serial
import random

ser = serial.Serial('COM5', 1152000, timeout=0.1)

while True:
  led_str = '{"led":[{"i":2, "m":1, "r":255, "b":255, "g":0}]}\n'
  ser.write(led_str.encode())
  for x in ser.readlines():
    print(x)
  time.sleep(0.5)

#  led_str = '{"led":[{"i":2, "m":0, "r":0, "b":255, "g":0}]}\n'
#  ser.write(led_str)
#  for x in ser.readlines():
#    print x
#  time.sleep(0.5)
#
#  led_str = '{"led":[{"i":2, "m":0, "r":255, "b":255, "g":255}]}\n'
#  ser.write(led_str)
#  for x in ser.readlines():
#    print x
#  time.sleep(0.5)
