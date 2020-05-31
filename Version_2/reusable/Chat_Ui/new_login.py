from PyQt5.QtWidgets import * #UI
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from captcha.image import ImageCaptcha
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout
import sys
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
import os


class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("Chat_box.ui", self) 
        self.textedit_messegebox = self.findChild(QTextEdit, "messegebox_t")
        # self.label = self.findChild(QLabel, "label")
        self.button_user = self.findChild(QPushButton, "user_b")
        self.button_send = self.findChild(QPushButton, "send_b")
        self.button_other = self.findChild(QPushButton, "other_b")
        self.button_clear = self.findChild(QPushButton, "clear_b")
        self.button_attach = self.findChild(QPushButton, "attach_b")
        self.button_record = self.findChild(QPushButton, "record_b")
        self.button_send.clicked.connect(self.clickedBtn_send)
        self.button_other.clicked.connect(self.clickedBtn_other) 
        self.button_clear.clicked.connect(self.clickedBtn_clear)   
        self.button_user.clicked.connect(self.clickedBtn_user)   
        self.textedit_messegebox.textChanged.connect(self.textChanged_messege_event)
        
       
        
        self.button_record.setHidden(False)
        self.button_send.setHidden(True)
      
       

        self.show()

   
        

    def clickedBtn_send(self):
        if self.textedit_messegebox.toPlainText().strip() :
            self.user_image = QLabel()
            self.user_image.setPixmap(QPixmap(os.path.abspath(os.getcwd()+'/me.png')).scaledToWidth(40))
            self.messege_user = QLabel(self.textedit_messegebox.toPlainText())
            self.messege_user.setStyleSheet("background-color: white;border: 2px solid teal;") 
            self.textedit_messegebox.clear()
            self.formLayout.addRow(self.user_image,self.messege_user)

    def clickedBtn_other(self):
        self.user_image = QLabel()
        self.user_image.setPixmap(QPixmap(os.path.abspath(os.getcwd()+'/other.png')).scaledToWidth(40))
        self.messege_user = QLabel(" salam mmd")
        self.messege_user.setStyleSheet("background-color: lightgreen;border: 1px solid teal;") 
        self.formLayout.addRow(self.user_image,self.messege_user)

    def clickedBtn_user(self):
        self.user_image = QLabel()
        self.user_image.setPixmap(QPixmap(os.path.abspath(os.getcwd()+'/other.png')).scaledToWidth(40))
        self.name_user = QLabel("\nMmd Hossein\n")
        self.name_user.setStyleSheet("background-color: white;border: 1px solid teal;") 
        self.formLayout_2.addRow(self.user_image,self.name_user)
        

    def textChanged_messege_event(self):
        
        if self.textedit_messegebox.toPlainText().strip() :
            self.button_record.setHidden(True)
            self.button_send.setHidden(False)
        else:
            self.button_record.setHidden(False)
            self.button_send.setHidden(True)


        
    def clickedBtn_clear(self):
        for i in reversed(range(self.formLayout.count())): 
            self.formLayout.itemAt(i).widget().deleteLater()
        


App = QApplication(sys.argv)
window2 = Window()
sys.exit(App.exec())