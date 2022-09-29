#!/usr/bin/env python3.3
import time
import serial
import sys


#12--red
#13--Yellow
#14--Green
#15--White
#16--blue
#17--Black
#18--red-command
#19--Yellow-command
#20--Green-command
#21--White-command
#22--blue-command
#23--Black-command
class palette_display:

    def __init__(self, perid_duration_in_seconds, alert_duration_in_seconds):
        self.peroid=perid_duration_in_seconds
        self.alert_duration=alert_duration_in_seconds
        self.ser = serial.Serial('COM5', 3000000, timeout=1, writeTimeout=None)
    # start screen transmission

    def set_green(self):
        holdthecolor = True
        while(holdthecolor):
            self.ser.write(('{"screen_display":' + str(14) + '}').encode("ascii"))
            time.sleep(self.period)
            holdthecolor=False
        holdthecolor=True

    def set_red(self):
        holdthecolor = True
        while(holdthecolor):
            self.ser.write(('{"screen_display":' + str(12) + '}').encode("ascii"))
            time.sleep(self.period)
            holdthecolor=False
        holdthecolor=True

    def set_yellow(self):
        holdthecolor = True

        while(holdthecolor):
            self.ser.write(('{"screen_display":' + str(13) + '}').encode("ascii"))
            time.sleep(self.period)
            holdthecolor=False
        holdthecolor=True

    def set_bliniking(self,i1,i2,duration):
        holdthecolor = True

        while(holdthecolor):
            for i in range(int(duration/0.1)):
                self.ser.write(('{"screen_display":' + str(i1) + '}').encode("ascii"))
                time.sleep(0.05)
                self.ser.write(('{"screen_display":' + str(i2) + '}').encode("ascii"))
                time.sleep(0.05)
            holdthecolor=False
        holdthecolor=True



    #12--red
    #13--Yellow
    #14--Green
    #15--White
    #16--blue
    #17--Black
    #18--red-command
    #19--Yellow-command
    #20--Green-command
    #21--White-command
    #22--blue-command
    #23--Black-command
    def show_message(self,state,duration):
        if(state=='green'):
            self.set_bliniking(20,21,duration)
        if(state=='red'):
            self.set_bliniking(18,21,duration)
        if(state=='yellow'):
            self.set_bliniking(19,23,duration)
        if(state=='blinking'):
            self.set_bliniking(18,23,duration)

    def close_port(self):
        self.ser.close()
