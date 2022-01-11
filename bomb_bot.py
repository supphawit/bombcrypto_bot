import pyautogui
import time
from datetime import datetime

pyautogui.FAILSAFE= True

def connect():
    find = pyautogui.locateOnScreen('images/connect.png', confidence=0.7)
    if find is not None:
        print("found connect")
        x, y = pyautogui.center(find)
        pyautogui.click(x/2,y/2) # for mac
        # pyautogui.click(x,y)
        time.sleep(3)
        sign = pyautogui.locateOnScreen('images/sign.png', confidence=0.7)
        if sign is not None:
            x, y = pyautogui.center(sign)
            # pyautogui.doubleClick(x,y)
            pyautogui.doubleClick(x/2,y/2) 
            # time.sleep(1)
            # metamask()
        connect()
    return    
    
def error():
    find = pyautogui.locateOnScreen('images/error.png', confidence=0.9)
    if find is not None:
        print("error")
        x, y = pyautogui.center(find)
        pyautogui.click(x,y)
        time.sleep(1)
        pyautogui.keyDown('shift')
        pyautogui.keyDown('command')
        pyautogui.press('r')
        error()
    return  

def hunt():
    print("hunt")
    find = pyautogui.locateOnScreen('images/hunt.png', confidence=0.8)
    if find is not None:
        x, y = pyautogui.center(find)
        pyautogui.click(x/2,y/2)
        time.sleep(0.5)
        hunt()
    return   

def back():
    print("back")
    find = pyautogui.locateOnScreen('images/back.png', confidence=0.8)
    if find is not None:
        x, y = pyautogui.center(find)
        pyautogui.click(x/2,y/2)
        time.sleep(0.2)
        back()
    return


def drag():
    print("drag")
    rim = pyautogui.locateOnScreen('images/rim.png', confidence=0.9)
    if (rim) is not None:
        # print("drag")
        x2, y2 =  pyautogui.center(rim) 
        pyautogui.click(x2/2,(y2/2)-50)
        time.sleep(0.5)
        pyautogui.dragTo(x2/2, (y2/2) - 800,duration=2, button='left') 
        drag()
    return


def hero():
    print("hero")
    find = pyautogui.locateOnScreen('images/hero.png', confidence=0.7)
    if find is not None:
        x, y = pyautogui.center(find)
        pyautogui.click(x/2,y/2)
        time.sleep(0.8)
        hero()
    return

def work():
    print("work")
    find = pyautogui.locateOnScreen('images/work.png', confidence=0.9)
    if find is not None :
        x, y = pyautogui.center(find)
        pyautogui.click((x/2)-10,y/2)
        # time.sleep(0.2)
        work()
    else:
        # time.sleep(3)
        close = pyautogui.locateOnScreen('images/close.png', confidence=0.8)
        if close is not None :
            x1, y1 = pyautogui.center(close)
            pyautogui.doubleClick(x1/2,y1/2)
            work()
        hunt = pyautogui.locateOnScreen('images/hunt.png', confidence=0.7)
        if hunt is not None :
            x2, y2 = pyautogui.center(hunt)
            pyautogui.doubleClick(x2/2,y2/2)
            work()
        # if close is not None and hunt is not None:
        #     return
    time.sleep(60)
    return

def new_map():
    print("new map")
    find = pyautogui.locateOnScreen('images/new_map.png', confidence=0.8)
    if find is not None:
        x, y = pyautogui.center(find)
        pyautogui.click(x/2,y/2)
        time.sleep(0.2)
        new_map()
    return

def reEnter():
    print("reEnter")
    now = datetime.now()
    current_minute = int(now.strftime("%M"))
    if current_minute % 3 == 0:
        back()
        hunt()
        time.sleep(60)
    return    

def daily():
    print("daily")
    back()
    hero()
    drag()
    work()
    return    

# work time 
work_time = 50
start = time.time()

while 1:
    print("start...")
    second = int( time.time() - start)
    print("time >>>>>>>> ", second)
    if(second >= (work_time * 60)):
        daily()
        start = time.time()
    connect()
    error()
    reEnter()
    hunt()
    new_map()
    print("end...")
    time.sleep(5)
