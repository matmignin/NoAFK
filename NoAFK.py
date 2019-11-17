import pyautogui as ag
import datetime as date
import time
import sys

ag.FAILSAFE = False
numMin = None
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 3
else:
    numMin = int(sys.argv[1])
while(True):
    x=0
    while(x<numMin):
        time.sleep(60)
        x+=1
    for i in range(0,200):
        ag.moveTo(0,i*4)
    pyautogui.moveTo(1,1)
    for i in range(0,3):
        ag.press("shift")
    print("Movement made at {}".format(datetime.now().time()))


JULIAN = ["0", "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M"]
YEAR = date.datetime.today().strftime("%y")
LOT = YEAR + "000"
BATCH = YEAR[1] + JULIAN[int(date.datetime.today().strftime("%m"))]

