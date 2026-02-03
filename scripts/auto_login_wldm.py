import subprocess
import time

import win32api
import win32gui
import win32process
import pyautogui as pya
from pyautogui import ImageNotFoundException

titles = {}
# Extractor for the accounts
with open(r"..\resources\account_names.txt","r") as file_account:
    for line in file_account:
        if line.startswith("#"):
            continue
        k,v = line.split(" ")
        titles[k] = v


# Put your Game's .exe file's path here.
APP = r"D:\Games\WDLPC20260113\WDLPC20260113\Wonderland M.exe"

def focus_win_with_title(title):
    win32gui.SetForegroundWindow(title)

def set_title_for_pid(pid, new_title, timeout=10):
    end = time.time() + timeout

    def enum_handler(hwnd, _):
        _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
        if found_pid == pid and win32gui.IsWindowVisible(hwnd):
            win32gui.SetWindowText(hwnd, new_title)

    while time.time() < end:
        win32gui.EnumWindows(enum_handler, None)
        time.sleep(0.2)

def click_with_certainty(img, x=None, y=None):
    # if it senses the image's match, it breaks, else continue for 10 times
    # to give more time on loading and rendering
    ret_click_coord = None
    for _ in range(10):
        try:
            ret_click_coord = pya.locateOnScreen(img, confidence=0.8)
            break
        except pya.ImageNotFoundException:
            time.sleep(1)
            continue
    if ret_click_coord is None:
        ''' for now, not raising an exception '''
        # raise pya.ImageNotFoundException
        return "not found"
    if x is not None:
        ret_click_coord_x = ret_click_coord[0] + x
    if y is not None:
        ret_click_coord_y = ret_click_coord[1] + y
    if x is None and y is None:
        pya.click(ret_click_coord)
        print("clicked without x or y")
    else:
        print("initial x=%d , y= %d" % (ret_click_coord[0], ret_click_coord[1]))
        pya.click(ret_click_coord_x,ret_click_coord_y)
        print("clicked with x=%d , y= %d" % (ret_click_coord_x, ret_click_coord_y))
        #exit(-1)




if __name__ == "__main__":
    for title in titles.keys():
        proc = subprocess.Popen([APP])
        time.sleep(1)
        set_title_for_pid(proc.pid, title)
        ''' Removed sleeps cause the function is gonna dyynamically sleep '''
        #time.sleep(3)

        click_with_certainty(r"..\resources\images\button_other_accounts.png")
        #time.sleep(2)
        click_with_certainty(r"..\resources\images\title_account.png", x=500, y=15)
        #print("writing")
        pya.typewrite(titles[title])
        #time.sleep(1)

        click_with_certainty(r"..\resources\images\button_login.png")
        #time.sleep(1)
        if click_with_certainty(r"..\resources\images\button_enter_game.png") is not None:
            raise ImageNotFoundException
        #time.sleep(1)
