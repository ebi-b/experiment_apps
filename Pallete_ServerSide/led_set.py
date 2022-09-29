#!/usr/bin/python
import time
import serial
import random

ser = serial.Serial('COM5', 1152000)

while True:
  led_str = '{"led":['
  for x in range(2,9):
    led_str += '{"i":'+str(x)+', "m":1, "r":'+str(random.randint(0,255))+', "g":'+str(random.randint(0,255))+', "b":'+str(random.randint(0,255))+' },'
  led_str = led_str[:-1]
  led_str += ']}\n'
  print(led_str)
  ser.write(led_str.encode())
  #print(led_str)
