import websockets
import asyncio
import os
import time
import serial
import threading
import datetime
import datetime
#ws=websocket.WebSocket()
#ws.connect("ws://localhost:59177/com.example.experiment/ExperimentConnection")
# STATES ARE 'green' 'yellow' 'red' 'blinking'
state='red'
last_submit=0
period_duration_in_seconds=20
alert_duration_in_seconds=10
data_is_not_inserted=True

class palette_display:

    def __init__(self, period_duration_in_seconds, alert_duration_in_seconds):
        #self.data_is_not_inserted=True
        self.state='green'
        self.period=period_duration_in_seconds
        self.alert_duration=alert_duration_in_seconds
        self.ser = serial.Serial('COM5', 3000000, timeout=1, writeTimeout=None)
        TrackerPath = r"c:\\Engagement-Challenge Experiment\\SlidersAndButtons"
        if not os.path.exists(TrackerPath):
            os.makedirs(TrackerPath)
        self.NotificationLogFile = open(TrackerPath + "\ Notification-" + str(time.time() * 1000) + ".txt", "a")

    # start screen transmission

    def set_green(self):
        print("Current State is Green.")
        tmp= str(time.time())+" : "+"Current State is Green. \n"
        self.NotificationLogFile.writelines(tmp)
        global data_is_not_inserted
        data_is_not_inserted=True
        #print("SETTING TO GREEN")
        for i in range(int(self.period/5)):
            self.ser.write(('{"screen_display":' + str(14) + '}').encode("ascii"))
            time.sleep(5)
        data_is_not_inserted=True

    def set_red(self):
        print("Current State is Red.")
        tmp = str(time.time()) + " : " + "Current State is Red. \n"
        self.NotificationLogFile.writelines(tmp)
        #print("SETTING TO RED")
        global data_is_not_inserted
        for i in range(int(self.period/5)):
            if data_is_not_inserted:
                self.ser.write(('{"screen_display":' + str(12) + '}').encode("ascii"))
                time.sleep(5)
            else:
                data_is_not_inserted=True
                global state
                state='green'
                break

    def set_yellow(self):
        print("Current State is Yellow.")
        tmp = str(time.time()) + " : " + "Current State is Yellow. \n"
        self.NotificationLogFile.writelines(tmp)
        self.NotificationLogFile.flush()
        #print("SETTING TO YELLOW")
        global data_is_not_inserted
        for i in range(int(self.period/5)):
            if data_is_not_inserted:
                self.ser.write(('{"screen_display":' + str(13) + '}').encode("ascii"))
                time.sleep(5)
            else:
                #print("IN YELLOW if")
                data_is_not_inserted=True
                global state
                state='green'
                break

    def set_bliniking(self,i1,i2,is_message):
        #print("SETTING TO BLINKING")
        global data_is_not_inserted
        if is_message == 0:
            tmp = str(time.time()) + " : " + "Current State is Blinking. \n"
            self.NotificationLogFile.writelines(tmp)
            self.NotificationLogFile.flush()
            print("Current State is Blinking.")
            duration = self.period
        else:
            duration = self.alert_duration

        for i in range(int(duration/0.2)):
            global data_is_not_inserted
            if data_is_not_inserted:
                #print("abasMASOOMI")
                self.ser.write(('{"screen_display":' + str(i1) + '}').encode("ascii"))
                time.sleep(0.1)
                self.ser.write(('{"screen_display":' + str(i2) + '}').encode("ascii"))
                time.sleep(0.1)
            else:
                #data_is_not_inserted=True
                global state
                state='green'
                break
        if is_message==1 and data_is_not_inserted:
            #print("state in blinking: "+state)
            if state=='green':
                state='yellow'
            elif state=='yellow':
                state='red'
            elif state=='red':
                state='blinking'
            elif state=='blinking':
                state='blinking'





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
    def show_message(self, state_when_enter_function):
        #print("SHOWING MESSAGE")
        if(state_when_enter_function== 'green'):
            print("Current State is Green Alert. \n")
            tmp = str(time.time()) + " : " + "Current State is Green Alert. \n"
            self.NotificationLogFile.flush()
            self.NotificationLogFile.writelines(tmp)
            self.NotificationLogFile.flush()
            self.set_bliniking(20,21,1)
        if(state_when_enter_function== 'red'):
            global state
            if state_when_enter_function==state:
                tmp = str(time.time()) + " : " + "Current State is Red Alert. \n"

                self.NotificationLogFile.writelines(tmp)
                self.NotificationLogFile.flush()
                print("Current State is Red Alert. \n")
                self.set_bliniking(18,21,1)

        if(state_when_enter_function== 'yellow'):
            if state_when_enter_function == state:
                print("Current State is Yellow Alert. \n")
                tmp = str(time.time()) + " : " + "Current State is Yellow Alert. \n"

                self.NotificationLogFile.writelines(tmp)
                self.NotificationLogFile.flush()

                self.set_bliniking(19,23,1)
        if(state_when_enter_function== 'blinking'):
            if state_when_enter_function == state:
                tmp = str(time.time()) + " : " + "Current State is Blinking Alert. \n"
                self.NotificationLogFile.writelines(tmp)
                print("Current State is Blinking Alert.")
                self.NotificationLogFile.flush()
                self.set_bliniking(18,23,1)


    def display_setup(self, state_when_enters_function):
        #print(state_when_enters_function)
        if state_when_enters_function== 'green':
            self.set_green()
            self.show_message(state_when_enters_function)
        if state_when_enters_function== 'yellow':
            self.set_yellow()
            self.show_message(state_when_enters_function)
        if state_when_enters_function== 'red':
            self.set_red()
            self.show_message(state_when_enters_function)
        if state_when_enters_function== 'blinking':
            self.set_bliniking(12,15,0)
            self.show_message(state_when_enters_function)


    def close_port(self):
        self.ser.close()

class input_thread(threading.Thread):
    def run(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        TrackerPath = r"c:\\Engagement-Challenge Experiment\\SlidersAndButtons"
        if not os.path.exists(TrackerPath):
            os.makedirs(TrackerPath)
        self.PalleteLogFile = open(TrackerPath + "\PalleteLogFiles-" + str(time.time() * 1000) + ".txt", "a")
        self.PalleteInterruptionLogFile = open(TrackerPath + "\PalleteInteruptionLogFiles-" + str(time.time() * 1000) + ".txt", "a")

        global last_submit
        last_submit=time.time()
        #print(last_submit)
        asyncio.get_event_loop().run_until_complete(self.test())

    async def test(self):
        async with websockets.connect("ws://localhost:59177/com.example.experiment/ExperimentConnection") as websocket:
            while (True):
                response = await websocket.recv()
                tmp = str(response)
                if tmp.find('Submit') != -1:
                    global last_submit
                    last_submit = time.time()
                    global data_is_not_inserted
                    data_is_not_inserted = False
                    print(last_submit)
                if tmp.find('Interuption') != -1:
                    self.PalleteInterruptionLogFile.writelines(str(datetime.datetime.now())+"\n")
                    self.PalleteInterruptionLogFile.flush()
                s = "Time Stamp: " + str(time.time() * 1000) + str(response)
                self.PalleteLogFile.writelines(s)
                print(s)

class display_thread(threading.Thread):


    def run(self):
        global period_duration_in_seconds
        p = period_duration_in_seconds
        global alert_duration_in_seconds
        a = alert_duration_in_seconds
        global state
        state='green'
        display = palette_display(p, a)
        while(True):
            #print(state)
            display.display_setup(state)
            #print('do')



    def detect_state(self):
        global period_duration_in_seconds
        p = period_duration_in_seconds
        global alert_duration_in_seconds
        a = alert_duration_in_seconds
        global state
        global last_submit
        now = time.time()
        dif = int(now - last_submit)
        if dif <= p:
            state = "green"
        elif dif <= 2 * p + a:
            state = "yellow"
        elif dif <= 3 * p + 2 * a:
            state = "red"
        elif dif >= 3 * p + 3 * a:
            state = "blinking"




period_duration = input("Insert the period duration! ")
alert_duration=input("Insert the alert duration! ")
#global period_duration_in_seconds
period_duration_in_seconds=int(period_duration)
#global alert_duration_in_seconds
alert_duration_in_seconds=int(alert_duration)


t=input_thread()
t.start()
d=display_thread()
d.start()
#dd=palette_display(10,15)
#dd.show_message('red')