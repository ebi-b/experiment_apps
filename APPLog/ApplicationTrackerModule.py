import win32gui
import time
import datetime
import os

class ApplicationTracker:

  global stopvar
  global logfile
  global  strapp
  def __init__(self, path):
    self.stopvar=True
    self.strapp = ""
    if not os.path.exists(path):
        os.makedirs(path)
    self.file = open(path+"Application Trackers.txt",'a',encoding="utf-8")


  def winEnumHandler(hwnd,slf):
    if win32gui.IsWindowVisible( hwnd ) and win32gui.GetWindowText(hwnd)!="":
      #print(slf.strapp)
      slf.strapp += str.format("{0},{1},{2},{3}--",hex(hwnd),win32gui.GetWindowText( hwnd ), win32gui.GetClassName(hwnd),win32gui.IsIconic(hwnd))
      #dsk=win32gui.GetDesktopWindow()
      #print(dsk)

  def application_logger(self,period_in_seconds):
    while(self.stopvar==False):
      now = time.time()*1000
      #print(now)
      foregroundText="Foreground Window:"+hex(win32gui.GetForegroundWindow())+","+win32gui.GetWindowText(win32gui.GetForegroundWindow())+"--"
      self.strapp=str.format("{0}-{1}",now,foregroundText)
      #print(self.strapp)
      hwnd=[]
      win32gui.EnumWindows(ApplicationTracker.winEnumHandler,self)
      print(self.strapp)
      self.strapp+='\n'
      self.file.write(self.strapp)
      self.file.flush()
      self.strapp = ""
      time.sleep(period_in_seconds)

  def start(self, period_in_sec):
    self.stopvar=False
    self.application_logger(period_in_sec)

  def stop(self):
    self.stopvar=True
