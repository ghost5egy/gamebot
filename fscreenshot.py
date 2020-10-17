import cv2 as cv
import numpy as np
import pyautogui
import win32gui
from time import time
import mss
import subprocess
import os

def getwindowlinux(wname):
    process = subprocess.Popen('wmctrl -l',shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    windowlist = process.stdout.read().decode('utf-8').lower()
    if windowlist.find(wname) != -1:
        process = subprocess.Popen('wmctrl -a ' + wname ,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        return True
    else:
        return False

def listwindowsnames():
	def winEnumHandler(hwnd, ctx):
		if win32gui.IsWindowVisible(hwnd):
			print(hex(hwnd), win32gui.GetWindowText(hwnd))
	win32gui.EnumWindows(winEnumHandler, None)

def getwindowwin(wname):
        hwnd = win32gui.FindWindow(None ,wname)
        listwindowsnames()
        return hwnd

def getwindow(wname):
    if os.name != 'nt':
        return getwindowlinux(wname)
    else:
        return getwindowwin(wname)


def windowcap():
    try:
        with mss.mss() as mss_instance:
            monitor_1 = mss_instance.monitors[1]
            screenshot = mss_instance.grab(monitor_1)
            img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX") 
            
    except:
        img = pyautogui.screenshot()
    
    img = np.array(img)
    img = img[:,:,::-1].copy()
    return img
    
ltime = time()
while True:
    sc = windowcap()
    cv.imshow('res', sc)

    print(1 / (time() - ltime))
    ltime = time()
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print(getwindow(None))
print('Exit')