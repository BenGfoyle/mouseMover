import win32api, win32con
import time
import random
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
while True:
    rMins = random.randint(1,10)
    time.sleep(60 * rMins)
    click(10,1080)
