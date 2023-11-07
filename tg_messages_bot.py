import pyautogui as pt
import pyperclip as pc
# from pynput.mouse import Controller, Button <--For mac
from time import sleep
from tg_responses import response
#Capture yours .png images for your bot (following images will not be compitable with your own program)
#Instruction for our TG bot
class Tele_bot:

    #Defines the starting values
    def __init__(self):
        self.message=''
        self.last_message=''

    #Navigate to the gray signs for new messages
    def nav_gray(self):
        try:
            position=pt.locateOnScreen('gray.png', confidence=.9)
            pt.moveTo(position)
            #pt.moveRel(25,-25) <--No need this
            #pt.rightClick() <--No need this
            #pt.rightClick() <--No need this
        except Exception as e:
            print('Exception (nav_gray):', e)

    #Copies the message to the program for analize
    def get_msg(self):
        pt.moveTo(427, 654)
        pt.rightClick()
        pt.rightClick()
        sleep(1)
        pt.hotkey('Ctrl', 'c')
        sleep(1)

        self.message=pc.paste()
        print('User says: ', self.message)

    #Sends the message to your friend
    def send_msg(self):
        try:
            #check whether the last message was the same
            if self.message != self.last_message:
                bot_response = response(self.message)
                print('You say:', bot_response)
                position=pt.locateOnScreen('paper.png', confidence=.7)
                pt.moveTo(position)
                #pt.moveRel(100,0) <--No need this
                pt.moveTo(462, 704)
                pt.rightClick()
                pt.typewrite(bot_response)
                pt.press('enter')

                #assigns the message that we consider now to the "last_message" for upcoming message
                self.last_message=self.message       
            else:
                print('No new messages..')

        except Exception as e:
            print('Exception (send_msg):', e)

        #close reply popup box when no new message receive
    def nav_x(self):
        try:
            position=pt.locateOnScreen('x.png', confidence=.7)
            pt.moveTo(position)
            pt.rightClick()
        except Exception as e:
            print('Exception (nav_x):', e)     

tg_bot=Tele_bot()
sleep(5)
while True:
    tg_bot.nav_gray()
    tg_bot.get_msg()
    tg_bot.send_msg()
    tg_bot.nav_x()
    sleep(5)
