#from ApplicationTrackerModule import ApplicationTracker
#at=ApplicationTracker("c:\\")
#at.start(10)
#import InsertRequestModule
#m= InsertRequestModule.insertRequest("Please Set The Sliders and Submit.", 1*60,10)
#m.start()
#print(m.lastMessageTime)

import tkinter as Tk
import win32gui
import client_gui

if __name__ == "__main__":
    root = Tk.Tk()
    toplevel= client_gui.New_Toplevel(root)
    root.mainloop()