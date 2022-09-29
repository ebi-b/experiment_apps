import tkinter as tk
import time
import os

class insertRequest:
    global message
    global period
    global lastMessageTime
    global contiueToShowMessages
    global duration_in_second

    def __init__(self, message,period_in_sec,duration_in_second):
        self.message = message
        self.period = period_in_sec
        self.lastMessageTime = 0
        self.contiueToShowMessages=False
        self.duration_in_second=duration_in_second
        path = "c:\\Engagement-Challenge Experiment\\Notification\\"
        if not os.path.exists(path):
            os.makedirs(path)
        self.file = open(path + "Notifications.txt", 'a', encoding="utf-8")

    def showMessage(self):
        root = tk.Tk()
        root.title("")
        root.geometry("300x100+1150+700")
        text=tk.Text()
        self.file.write(str(time.time())+"\n")
        self.file.flush()
        root['font']=text.configure(font=("Times New Roman", 70, "bold"))
        tk.Label(root, text=self.message,).pack()
        root.after(self.duration_in_second*1000, lambda: root.destroy())  # time in ms
        self.lastMessageTime = time.time()
        root.mainloop()

    def start(self):
        self.contiueToShowMessages=True
        while(self.contiueToShowMessages):
            self.showMessage()
            time.sleep(self.period)
