import ApplicationTrackerModule as appTracker
import InsertRequestModule as notif
import MouseKeyboardListenerModule as kmTracker
import threading
import EyeTrackerModule



try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import client_gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    client_gui_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    client_gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    global roott
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("600x450+650+150")
        top.title("Starting UI")
        top.configure(background="#d9d9d9")
        self.roott=top


        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.033, rely=0.044, relheight=0.922, relwidth=0.942)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=565)

        self.eyeButton = Button(self.Frame1)
        self.eyeButton.place(relx=0.655, rely=0.048, height=53, width=166)
        self.eyeButton.configure(activebackground="#d9d9d9")
        self.eyeButton.configure(activeforeground="#000000")
        self.eyeButton.configure(background="#d9d9d9")
        self.eyeButton.configure(disabledforeground="#a3a3a3")
        self.eyeButton.configure(foreground="#000000")
        self.eyeButton.configure(highlightbackground="#d9d9d9")
        self.eyeButton.configure(highlightcolor="black")
        self.eyeButton.configure(pady="0")
        self.eyeButton.configure(text='''Start Eye Tracker''')
        self.eyeButton.configure(width=166)
        self.eyeButton.configure(command=self.eyebuttonhandler)

        self.kmButton = Button(self.Frame1)
        self.kmButton.place(relx=0.655, rely=0.265, height=63, width=166)
        self.kmButton.configure(activebackground="#d9d9d9")
        self.kmButton.configure(activeforeground="#000000")
        self.kmButton.configure(background="#d9d9d9")
        self.kmButton.configure(disabledforeground="#a3a3a3")
        self.kmButton.configure(foreground="#000000")
        self.kmButton.configure(highlightbackground="#d9d9d9")
        self.kmButton.configure(highlightcolor="black")
        self.kmButton.configure(pady="0")
        self.kmButton.configure(text='''Start K/M Logger''')
        self.kmButton.configure(width=166)
        self.kmButton.configure(command=self.kmbuttonhandler)

        self.appTrackerButton = Button(self.Frame1)
        self.appTrackerButton.place(relx=0.655, rely=0.506, height=63, width=166)
        self.appTrackerButton.configure(activebackground="#d9d9d9")
        self.appTrackerButton.configure(activeforeground="#000000")
        self.appTrackerButton.configure(background="#d9d9d9")
        self.appTrackerButton.configure(disabledforeground="#a3a3a3")
        self.appTrackerButton.configure(foreground="#000000")
        self.appTrackerButton.configure(highlightbackground="#d9d9d9")
        self.appTrackerButton.configure(highlightcolor="black")
        self.appTrackerButton.configure(pady="0")
        self.appTrackerButton.configure(text='''Start App Tracker''')
        self.appTrackerButton.configure(width=166)
        self.appTrackerButton.configure(command=self.apptrackerbuttonhandler)

        self.notbutton = Button(self.Frame1)
        self.notbutton.place(relx=0.655, rely=0.747, height=63, width=166)
        self.notbutton.configure(activebackground="#d9d9d9")
        self.notbutton.configure(activeforeground="#000000")
        self.notbutton.configure(background="#d9d9d9")
        self.notbutton.configure(disabledforeground="#a3a3a3")
        self.notbutton.configure(foreground="#000000")
        self.notbutton.configure(highlightbackground="#d9d9d9")
        self.notbutton.configure(highlightcolor="black")
        self.notbutton.configure(pady="0")
        self.notbutton.configure(text='''Start Notifications''')
        self.notbutton.configure(width=166)
        self.notbutton.configure(command=self.notbuttonhandler)

        self.hidebutton = Button(self.Frame1)
        self.hidebutton.place(relx=0.106, rely=0.747, height=63, width=166)
        self.hidebutton.configure(activebackground="#d9d9d9")
        self.hidebutton.configure(activeforeground="#000000")
        self.hidebutton.configure(background="#d9d9d9")
        self.hidebutton.configure(disabledforeground="#a3a3a3")
        self.hidebutton.configure(foreground="#000000")
        self.hidebutton.configure(highlightbackground="#d9d9d9")
        self.hidebutton.configure(highlightcolor="black")
        self.hidebutton.configure(pady="0")
        self.hidebutton.configure(text='''Hide''')
        self.hidebutton.configure(command=self.hidebuttonhandler)

    def startkm(self):
        kmTracker.MouseKeyboardListener().start(kmTracker.MouseKeyboardListener)

    def startapptracker(self):
        appTracker.ApplicationTracker("c:\\Engagement-Challenge Experiment\\AppTracker\\").start(10)

    def startnotif(self):
        notif.insertRequest("Please Insert Your Engagement and Challenge Level", 60, 5).start()

    def starteyetracker(self):
        EyeTrackerModule.eyetracker().start("eyetracker-Runner\\eyetracker-Runner\\bin\\Debug\\eyetracker-Runner.exe")

    class myThread(threading.Thread):
        def __init__(self, threadID, name, counter):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.counter = counter

        def run(self):
            if (self.name == "km"):
                New_Toplevel.startkm(self)
            if (self.name == "n"):
                New_Toplevel.startnotif(self)
            if (self.name == "a"):
                New_Toplevel.startapptracker(self)
            if (self.name == "e"):
                New_Toplevel.starteyetracker(self)


    def kmbuttonhandler(self):
        New_Toplevel.myThread(1,"km",1).start()
    def notbuttonhandler(self):
        New_Toplevel.myThread(2,"n",2).start()
    def apptrackerbuttonhandler(self):
        New_Toplevel.myThread(3,"a",3).start()
    def eyebuttonhandler(self):
        New_Toplevel.myThread(4,"e",4).start()
    def hidebuttonhandler(self):
        #print("do nothing")
        self.roott.withdraw()



