
import socket
import time
import os
import IPython.display as display
import pyscreenshot as ImageGrab
import alsaaudio
##
from PyQt5.QtWidgets import * #UI
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from captcha.image import ImageCaptcha
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5 import QtCore 
from PyQt5.QtCore import Qt 
import sys 
from PyQt5.QtGui import QColor
import os
import datetime
import time
from PyQt5.QtCore import QTimer
import cv2
# import pygame
from PyQt5.QtCore import QTimer
####

class window_r(QMainWindow):
    last_used = ""
    def __init__(self):
        super().__init__()
        uic.loadUi("remote.ui", self) 
        self.vol_d.clicked.connect(self.clickedBtn_voldown)
        self.vol_u.clicked.connect(self.clickedBtn_volup)
        self.show()
        self.start_e()
        
    

    def clickedBtn_volup(self):
        m = alsaaudio.Mixer()
        if (int(m.getvolume()[0])<=95):
            
            m.setvolume(abs(int(m.getvolume()[0])+5))
            print(m.getvolume()[0])
    
    def clickedBtn_voldown(self):
        m = alsaaudio.Mixer()
        if (int(m.getvolume()[0])>=4):
           
            m.setvolume(abs(int(m.getvolume()[0])-5))
            
                        

    def start_e(self):
        while True:
            img = ImageGrab.grab()
            img.save("rec.jpg")

            
            self.show_r_l.setPixmap(QPixmap(os.path.abspath(os.getcwd()+"/rec.jpg")))
            app.processEvents()

app = QApplication(sys.argv)
window = window_r()
sys.exit(app.exec())

