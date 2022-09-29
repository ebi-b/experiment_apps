#!/usr/bin/python
import time
import sys
import serial
import random
import time
from threading import Thread
from midiPalleteModule import midiPallete

class Pallete:

    def __init__(self,Port):
        self.ser = serial.Serial(Port, 1152000)
        self.blink=True
    def start_blinking(self):
        self.blink=True
        print("HEre")
        Thread
        while(self.blink):
          led_str = '{"led":['
          for x in range(2,9):
            led_str += '{"i":'+str(x)+', "m":0, "r":'+"255"+', "g":'+"0"+', "b":'+"0"+' },'
          led_str = led_str[:-1]
          led_str += ']}\n'
          self.ser.write(led_str.encode())
          #print("1:"+led_str)
          time.sleep(1)
          led_str = '{"led":['
          for x in range(2,9):
            led_str += '{"i":'+str(x)+', "m":0, "r":'+"255"+', "g":'+"255"+', "b":'+"255"+' },'
          led_str = led_str[:-1]
          led_str += ']}\n'
          self.ser.write(led_str.encode())
          #print("2:"+led_str)
          time.sleep(1)
    def stop_blinking(self):
        self.blink=False
        led_str = '{"led":['
        for x in range(2, 9):
            led_str += '{"i":' + str(x) + ', "m":0, "r":' + "0" + ', "g":' + "255" + ', "b":' + "0" + ' },'
        led_str = led_str[:-1]
        led_str += ']}\n'
        self.ser.write(led_str.encode())
    def set_colors(self,lastInsertlevel):
        if lastInsertlevel==0:
            print("set Green")
            led_str = '{"led":['
            for x in range(2, 9):
                led_str += '{"i":' + str(x) + ', "m":0, "r":' + "0" + ', "g":' + "255" + ', "b":' + "0" + ' },'
            led_str = led_str[:-1]
            led_str += ']}\n'
            self.ser.write(led_str.encode())

        if lastInsertlevel==1:
            print("set white")
            led_str = '{"led":['
            for x in range(2, 9):
                led_str += '{"i":' + str(x) + ', "m":0, "r":' + "255" + ', "g":' + "255" + ', "b":' + "255" + ' },'
            led_str = led_str[:-1]
            led_str += ']}\n'
            self.ser.write(led_str.encode())

        if lastInsertlevel==2:
            print("set yellow")
            led_str = '{"led":['
            for x in range(2, 9):
                led_str += '{"i":' + str(x) + ', "m":0, "r":' + "0" + ', "g":' + "255" + ', "b":' + "255" + ' },'
            led_str = led_str[:-1]
            led_str += ']}\n'
            self.ser.write(led_str.encode())

        if lastInsertlevel==3:
            print("set orange")
            led_str = '{"led":['
            for x in range(2, 9):
                led_str += '{"i":' + str(x) + ', "m":0, "r":' + "255" + ', "g":' + "153" + ', "b":' + "51" + ' },'
            led_str = led_str[:-1]
            led_str += ']}\n'
            self.ser.write(led_str.encode())

        if lastInsertlevel==5:
            print("set red")
            led_str = '{"led":['
            for x in range(2, 9):
                led_str += '{"i":' + str(x) + ', "m":0, "r":' + "255" + ', "g":' + "0" + ', "b":' + "0" + ' },'
            led_str = led_str[:-1]
            led_str += ']}\n'
            self.ser.write(led_str.encode())

        if lastInsertlevel==6:
          print("blink")
          p=PalleteThreads(self,"blinking")
          p.start()




class PalleteThreads(Thread):

    def __init__(self,pallete_obj,type):
        Thread.__init__(self)
        self.type = type
        self.palleteObj = pallete_obj
        #print("JOOD")

    def run(self):
        if(self.type=="blinking"):
            #print("ANAS")
            self.palleteObj.start_blinking()


if __name__ == '__main__':
    p=Pallete("COM4")
    m=midiPallete()
    device_id = int(sys.argv[-1])

    #t=PalleteThreads(p, "blinking")
    #t.start()
    #p.start_blinking()
    #time.sleep(10)
    #p.stop_blinking()
    #time.sleep(10)
    #p.set_colors(6)
    #for i in range(0,7):
     #   p.set_colors(i)
      #  time.sleep(3)
    # #p.stop_blinking()


