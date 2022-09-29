#!/usr/bin/env python3.3
import time

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
import serial as serial


class palette_display:

    def __init__(self, period_duration_in_seconds, alert_duration_in_seconds):
        self.data_is_not_inserted=True
        self.period=period_duration_in_seconds
        self.alert_duration=alert_duration_in_seconds
        self.ser = serial.Serial('COM5', 3000000, timeout=1, writeTimeout=None)
    # start screen transmission

    def set_green(self):
        print("SETTING TO GREEN")
        for i in range(int(self.period/5)):
            self.ser.write(('{"screen_display":' + str(14) + '}').encode("ascii"))
            time.sleep(5)

    def set_red(self):
        print("SETTING TO RED")
        for i in range(int(self.period/5)):
            self.ser.write(('{"screen_display":' + str(12) + '}').encode("ascii"))
            time.sleep(5)

    def set_yellow(self):
        print("SETTING TO YELLOW")
        for i in range(int(self.period/5)):
            self.ser.write(('{"screen_display":' + str(13) + '}').encode("ascii"))
            time.sleep(5)

    def set_bliniking(self,i1,i2,is_message):
        print("SET TO BLINKING")
        if is_message == 0:

            duration = self.period
        else:
            duration = self.alert_duration
        for i in range(int(duration/0.1)):
            if self.data_is_not_inserted:
                self.ser.write(('{"screen_display":' + str(i1) + '}').encode("ascii"))
                time.sleep(0.05)
                self.ser.write(('{"screen_display":' + str(i2) + '}').encode("ascii"))
                time.sleep(0.05)
            else:
                self.data_is_not_inserted=True
                break


    def data_is_inserted(self):
        self.data_is_not_inserted=False


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
    def show_message(self,state):
        print("MESSAGE IS SHOWING")
        if(state=='green'):
            self.set_bliniking(20,21,1)
        if(state=='red'):
            self.set_bliniking(18,21,1)
        if(state=='yellow'):
            self.set_bliniking(19,23,1)
        if(state=='blinking'):
            self.set_bliniking(18,23,1)


    def display_setup(self, state):
        if state=='green':
            self.set_green()
            self.show_message(state)
        if state=='yellow':
            self.set_yellow()
            self.show_message(state)
        if state=='red':
            self.set_red()
            self.show_message(state)
        if state=='blinking':
            self.set_bliniking(12,15,0)
            self.show_message(state)


    def close_port(self):
        self.ser.close()
