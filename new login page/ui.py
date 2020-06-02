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


class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()

        # with open("theme.txt") as file: # Use file to refer to the file object
        #     data = file.read()
        #     print (data)
            


        uic.loadUi("untitled.ui", self)


        # self.Username_LE.setStyleSheet("background-color: white;border: 1px solid teal;border-radius:15px;") 
        # self.Password_LE.setStyleSheet("background-color: white;border: 1px solid teal;border-radius:15px;") 
        # self.Signin_BTN.setStyleSheet("background-color: white;border: 1px solid teal;border-radius:15px;") 
        # self.Signup1_BTN.setStyleSheet("background-color: rgb(58, 175, 159);border: 1px solid teal;border-radius:15px;") 

        # self.Signin_FRM.setStyleSheet("border-radius:15px;") 
        # self.Signup_FRM.setStyleSheet("border-radius:15px;") 



        self.Signup1_BTN.clicked.connect(self.Go_to_signup)
        self.pushButton.clicked.connect(self.Back_from_signup_to_signin)
        self.Forgotpass_BTN_2.clicked.connect(self.Go_to_recovery)
        self.Signin_BTN_2.clicked.connect(self.Go_to_varify)
        self.Signup1_BTN_2.clicked.connect(self.Go_to_changepass)



        self.show()



    def Go_to_signup(self):
        self.Signin_FRM.setGeometry(QtCore.QRect(22000,0, 801, 541))#dge nabayad to x=22000 ui bezaram chon mishe zir majmoaash
        self.Signup_FRM.setGeometry(QtCore.QRect(0,0, 801, 541))


    def Back_from_signup_to_signin(self):
        self.Signup_FRM.setGeometry(QtCore.QRect(22000,0, 801, 541))
        self.Signin_FRM.setGeometry(QtCore.QRect(0,0, 801, 541))


    def Go_to_recovery(self):
        self.Signin_FRM.setGeometry(QtCore.QRect(-1000,0, 801, 541))
        self.Recover_FRM.setGeometry(QtCore.QRect(0,0, 801, 541))


    def Go_to_varify(self):
        self.Recover_FRM_2.setGeometry(QtCore.QRect(0,0, 801, 541))


    def Go_to_changepass(self):
        self.Recover_FRM_3.setGeometry(QtCore.QRect(0,0, 801, 541))














    
        


App = QApplication(sys.argv)
window2 = Window()
sys.exit(App.exec())