#This file is used to capture mouse actions
import csv
import datetime
import time
import os
from pynput.mouse import Listener as mouseListener
from pynput.keyboard import Listener as keyboardListener


class MouseKeyboardListener:
    TrackerPath = r'C:\Trackers Folder'
    if not os.path.exists(TrackerPath):
        os.makedirs(TrackerPath)

    keyboardLogFile = open(TrackerPath+"\keyboardLogFile.txt", "a")
    #keyboardLogFileWriter = csv.writer(keyboardLogFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    mouseLogFile = open(TrackerPath+"\mouseLogFile.txt", "a")
    #mouseLogFileWriter = csv.writer(mouseLogFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    def __init__(self):
        print("Mouse & Keyboard Listener is Created")
        #print('Closed',self.keyboardLogFile.closed)
        #self.keyboardLogFile = open(r"c:\keyboardLogFile.csv", "w+")
        #self.keyboardLogFileWriter = csv.writer(self.keyboardLogFile, delimiter=',', quotechar='|',
        #                                        quoting=csv.QUOTE_MINIMAL)
        #self.keyboardLogFileWriter.writerow(['Date', 'Time[ms]', 'Key', 'Pressed/Release'])
        #self.mouseLogFile = open(r"c:\mouseLogFile.csv", "w+")
        #self.mouseLogFileWriter = csv.writer(self.mouseLogFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #self.mouseLogFileWriter.writerow(['Date', 'Time[ms]', 'Click/Scroll/Move', 'X', 'Y', 'Click[Button]',
        #                                  'Click[Pressed/Released]', 'Scroll[dx]', 'Scroll[dy]'])
#------------------------------------------------------------------------------------------------------------------------------#
    @staticmethod
    def start(self):
        print('Closed', self.keyboardLogFile.closed)
        # self.keyboardLogFileWriter.writerow(['Date', 'Time[ms]', 'Key', 'Pressed/Release'])
        with mouseListener(on_click=MouseKeyboardListener.on_mouse_click, on_move=MouseKeyboardListener.on_mouse_move, on_scroll=MouseKeyboardListener.on_mouse_scroll) as mouse_listener,\
                keyboardListener(on_press=MouseKeyboardListener.on_keyboard_press, on_release=MouseKeyboardListener.on_keyboard_release) as keyboard_listener:
                        self.keyboardLogFile.write("REZZ")
                        mouse_listener.join()
                        keyboard_listener.join()

#_________________________________________________________________________________________________________________________________________________________________#
#----------------------------------------------------------------------------------------------------------------------#
    def on_mouse_move(x, y):
        #MouseKeyboardListener.on_mouse_move_write(x, y)
        MouseKeyboardListener.mouseLogFile.write(str(datetime.datetime.now())+","+str(time.time()*1000)+","+'M'+","+ str(x)+","+ str(y) +","+ 'NULL'+","+'NULL'+","+'NULL'+","+'NULL'+"\n")
        MouseKeyboardListener.mouseLogFile.flush()
    def on_mouse_click(x, y, button, pressed):
        #MouseKeyboardListener.on_mouse_click_write(x, y, button, pressed)
        MouseKeyboardListener.mouseLogFile.write(str(datetime.datetime.now())+','+str(time.time()*1000)+','+'C'+',' +str(x) +',' + str(y) +',' + str(button)+',' +'P' if pressed else 'R'+',' +'NULL'+',' +'NULL'+"\n")
        MouseKeyboardListener.mouseLogFile.flush()
    def on_mouse_scroll(x, y, dx, dy):

        MouseKeyboardListener.mouseLogFile.write(str(datetime.datetime.now())+","+ str(time.time()*1000)+","+ 'S'+","+ str(x) +","+ str(y) +","+ 'NULL'+","+'NULL'+","+str(dx)+","+str(dy)+"\n")
        MouseKeyboardListener.mouseLogFile.flush()
        #MouseKeyboardListener.on_mouse_scroll_write(x, y, dx, dy)
        # print('Scrolled {0} at {1}'.format(
        #   'down' if dy < 0 else 'up',
        #  (x, y)))

    def on_keyboard_press(x):
        #MouseKeyboardListener.on_keyboard__press_write(x)
        MouseKeyboardListener.keyboardLogFile.write(str(datetime.datetime.now())+','+ str(time.time()*1000)+','+str(x)+','+'P'+"\n")
        MouseKeyboardListener.keyboardLogFile.flush()
    def on_keyboard_release(x):
        MouseKeyboardListener.keyboardLogFile.write(str(datetime.datetime.now())+','+ str(time.time()*1000)+','+str(x)+','+'R'+"\n")
        MouseKeyboardListener.keyboardLogFile.flush()
        #MouseKeyboardListener.on_keyboard__release_write(x)