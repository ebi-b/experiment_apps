#!/usr/bin/python
import time
import serial
import random

ser = serial.Serial('COM5', 1152000, timeout=1)

led_str = '{"led":['
for x in range(2,9):
  led_str += '{"i":'+str(x)+', "m":0, "r":'+str(random.randint(254,255))+', "g":'+str(random.randint(0,1))+', "b":'+str(random.randint(0,1))+' },'
led_str = led_str[:-1]
led_str += ']}\n'
ser.write(led_str.encode())
print(ser.readlines())
