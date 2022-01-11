import threading

import tkinter as tk
from PIL import Image
from pystray import MenuItem as item
import pystray

import pyautogui
import win32api
import time
from datetime import datetime

import tools

class jerry:
    def __init__(self):
        # Tray
        icon=Image.open(tools.resource_path("cheese_icon.ico"))
        tray_menu=(item('Quit', self.stop_and_quit),)
        self.tray_icon=pystray.Icon("jerry", icon, "Jerry the mouse", tray_menu)

        # Variables
        self.iddleTime = 3
        self.eachMin = self.iddleTime / 4
        self.wake_up = True
    
    def getIdleTime(self):
        return (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0
    
    def run(self):
        thread_for_tray = threading.Thread(target=self.tray_icon.run, args=())
        thread_for_tray.start()

    def wake_up_routine(self):
        while(self.wake_up):
            time.sleep(self.eachMin * 60)
            print("Idle from {}".format(self.getIdleTime() / 60))
            if self.getIdleTime() / 60 > self.iddleTime:
                pyautogui.press("shift")
                print("Wake up at {}".format(datetime.now()))

    def stop_and_quit(self):
        self.tray_icon.stop()
        self.wake_up = False


if __name__ == '__main__':
    app = jerry()
    app.run()
    app.wake_up_routine()
    