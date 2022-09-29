

from MouseKeyboardListenerModule import MouseKeyboardListener as MouseKeyboardListener
import GUI
import GUI_support
from tkinter import *


def main():
    # Starting the UI
    global root
    root = Tk()
    GUI_support.set_Tk_var()
    gui = GUI.New_Toplevel(root)
    GUI_support.init(root, gui)
    root.mainloop()
    # End of Starting UI
    x = MouseKeyboardListener()
    x.start(self=x)


if __name__ == '__main__':
    main()




