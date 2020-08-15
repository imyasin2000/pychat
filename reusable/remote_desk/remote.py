
# import getch
# char = getch.getch()
# print(char)
# #read from keyboard

# import pyautogui 
# pyautogui.write('Hello world!')
# #write to keyboard

# pyautogui.moveTo(100,100,duration=1.5)
# #move mouse

# print(pyautogui.position())
# #read mouse position    

    
import os
import subprocess,sys

file =os.path.abspath(os.getcwd()+'/output2.png')


opener ="open" if sys.platform == "darwin" else "xdg-open"
subprocess.call([opener, file])

