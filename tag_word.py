import pyautogui as pt
import time
import pyperclip
import random
#This is simple example, I uploaded a little bit expanded version of this program to main
#Set delay to start program
time.sleep(3)
#this a auto chat program for telegram it will auto reply something, (you writting in 20 line)
#if someone send you message like "mmm". This program automatically re-type "mmm" and reply
def check_newmsg():
    pos2 = pt.locateOnScreen("paper.png", confidence=.7)

    while True:
        try:
            pos1 = pt.locateOnScreen("mmm.png", confidence=.9)

            if pos1 is not None:
                pt.moveTo(pos2)
                pt.moveRel(+100, 0)
                pt.click()
                pt.typewrite("mmm") #tagged word for "Mmm"
                pt.press("Enter")
                
        except():
                print("No new messages")

check_newmsg()
