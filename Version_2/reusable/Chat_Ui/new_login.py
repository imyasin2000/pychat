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



class Window(QMainWindow):
    last_used = ""
    def __init__(self):
        super().__init__()

        # with open("theme.txt") as file: # Use file to refer to the file object
        #     data = file.read()
        #     print (data)
            


        uic.loadUi("Chat_box.ui", self) 
        self.setStyleSheet("QWidget { background-color: %s}" % QtGui.QColor(252, 255, 253).name())
        self.textedit_messegebox = self.findChild(QTextEdit, "messegebox_t")
        self.textedit_usersearch= self.findChild(QTextEdit, "user_search_t")
        # self.label = self.findChild(QLabel, "label")
        self.button_user = self.findChild(QPushButton, "user_b")
        self.button_send = self.findChild(QPushButton, "send_b")
        self.button_other = self.findChild(QPushButton, "other_b")
        self.button_clear = self.findChild(QPushButton, "clear_b")
        self.button_attach = self.findChild(QPushButton, "attach_b")
        self.button_record = self.findChild(QPushButton, "record_b")
        self.button_menu = self.findChild(QPushButton, "menu_b")
        self.button_usersearch= self.findChild(QPushButton, "user_search_b")
        self.label_sidebar = self.findChild(QLabel, "side_bar_l")
        self.label_topchatbar = self.findChild(QLabel, "topchat_bar_l")
        self.label_bottomchatbar = self.findChild(QLabel, "bottomchat_bar_l")
        
        self.label_usernamem = self.findChild(QLabel, "usernamem_l")
        self.label_lastseen = self.findChild(QLabel, "lastseen_l")
        self.button_menu_user= self.findChild(QPushButton, "menu_user_b")
        self.button_searchuser= self.findChild(QPushButton, "searchuser_b")
        self.button_call= self.findChild(QPushButton, "call_b")


        self.label_background = self.findChild(QLabel, "background_l")
        self.label_background.setPixmap(QPixmap(os.path.abspath(os.getcwd()+'/icons/background.png')))
        

        self.button_menu_user.setStyleSheet("background-color: transparent;border: 1px solid transparent;") 
        self.button_searchuser.setStyleSheet("background-color: transparent;border: 1px transparent;")
        self.button_call.setStyleSheet("background-color: transparent;border: 1px transparent;")
        self.label_lastseen.setStyleSheet("background-color: transparent;border: 1px solid transparent;")
        self.label_usernamem.setStyleSheet("background-color: transparent;border: 1px solid transparent;")
       
        self.label_bottomchatbar.setStyleSheet("QWidget { background-color: %s}" % QtGui.QColor(255, 255, 255).name())
        self.label_topchatbar.setStyleSheet("QWidget { background-color: %s}" % QtGui.QColor(255, 255, 255).name())
        self.label_sidebar.setStyleSheet("QWidget { background-color: %s};border: 1px solid white;" % QtGui.QColor(1, 36, 32).name())
        self.label_bottomchatbar.setStyleSheet("border: 1px solid lightgray;")
        self.label_topchatbar.setStyleSheet("border: 1px solid lightgray;")
        
        self.button_menu.setStyleSheet("background-color: white;border: 1px solid white;border-radius:15px;")

        self.button_record.setStyleSheet("background-color: transparent;border: 1px solid white;border-radius:15px;") 
        self.button_send.setStyleSheet("background-color: transparent;border: 1px solid white;border-radius:15px;") 
        self.button_attach.setStyleSheet("background-color: transparent;border: 1px solid white;border-radius:15px;") 
        self.textedit_messegebox.setStyleSheet("background-color: white;border: 1px solid lightgray;border-radius:15px;") 
        self.button_usersearch.setStyleSheet("background-color: white;border: 1px solid white;") 
        self.textedit_usersearch.setStyleSheet("background-color: white;border: 1px solid gray;border-radius:15px;") 
        
        self.button_menu_user.setIcon(QIcon(os.getcwd()+'/icons/menu_user.png'))
        self.button_searchuser.setIcon(QIcon(os.getcwd()+'/icons/search.png'))
        self.button_call.setIcon(QIcon(os.getcwd()+'/icons/phone.png'))

        self.button_usersearch.setIcon(QIcon(os.getcwd()+'/icons/search.png'))
        self.button_menu.setIcon(QIcon(os.getcwd()+'/icons/menu.png'))
        self.button_record.setIcon(QIcon(os.getcwd()+'/icons/radio.png'))
        self.button_attach.setIcon(QIcon(os.getcwd()+'/icons/clip.png')) 
        self.button_send.setIcon(QIcon(os.getcwd()+'/icons/send.png'))  

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
            massege_text="\n   "
            self.user_image = QLabel()
            self.user_image.setPixmap(QPixmap(os.path.abspath(os.getcwd()+'/icons/me.png')).scaledToWidth(35))
            if len(self.textedit_messegebox.toPlainText())<=66:
                self.messege_user = QLabel("   " + self.textedit_messegebox.toPlainText(),self)
            else:    
                i=0
                while(len(massege_text)-8<=len(self.textedit_messegebox.toPlainText())):
                    
                    massege_text=massege_text+self.textedit_messegebox.toPlainText()[i:i+66]+"\n   "
                    i=66+i
                self.messege_user = QLabel(massege_text,self)

                

            
            
            self.messege_user.setStyleSheet("background-color: #D7FAB3;border: 0px solid lightgray;border-radius: 17px;") 
            if self.last_used == "other" :
                self.formLayout.addRow(QLabel())
                
            self.textedit_messegebox.clear()
            self.formLayout.addRow(self.user_image,self.messege_user)
            self.messege_time = QLabel(" 12:54 ",alignment=Qt.AlignRight)
            self.messege_time.setStyleSheet("color: black")
            self.messege_time.setStyleSheet("background-color: white;border: 0px solid lightgray;border-radius: 5px;") 
            self.seen_image = QLabel()
            self.seen_image.setPixmap(QPixmap(os.path.abspath(os.getcwd()+'/icons/not_seen.png')).scaledToWidth(20))
            self.formLayout.addRow(self.messege_time,self.seen_image)
            self.last_used="me"

    def clickedBtn_other(self):
        self.user_image = QLabel()
        self.user_image.setPixmap(QPixmap(os.path.abspath(os.getcwd()+'/icons/user.png')).scaledToWidth(35))
        self.messege_user = QLabel("\n   salam mmd"+"\n                                                                                                                               "+datetime.datetime.now().strftime("%H:%M"))
        self.messege_user.setStyleSheet("background-color: white;border: 1px solid lightgray;border-radius: 17px;")

        
        if self.last_used == "me" :
            self.formLayout.addRow(QLabel())
            
        self.formLayout.addRow(self.user_image,self.messege_user)

        self.last_used="other"

    def clickedBtn_user(self):
        self.user_image = QLabel()
        self.user_image.setPixmap(QPixmap(os.path.abspath(os.getcwd()+'/icons/icon.png')).scaledToWidth(30))
        self.user_image.setStyleSheet("")
        self.name_user = QLabel("\n Mmd Hossein\n")
        self.name_user.setStyleSheet("background-color: white;border: 1px solid black;border-radius: 10px;") 
        self.formLayout_2.addRow(self.user_image,self.name_user)
        # self.formLayout_2.addRow(QLabel(''))
          

    def textChanged_messege_event(self):
        
        if self.textedit_messegebox.toPlainText().strip() :
            self.button_record.setHidden(True)
            self.button_send.setHidden(False)
        else:
            self.button_record.setHidden(False)
            self.button_send.setHidden(True)


        
    def clickedBtn_clear(self):
        # for i in reversed(range(self.formLayout.count())): 
        #     self.formLayout.itemAt(i).widget().deleteLater()
        for i in reversed(range(self.formLayout.count())): 
            self.formLayout.itemAt(3).widget().setPixmap(QPixmap(os.path.abspath(os.getcwd()+'/icons/seen.png')).scaledToWidth(30)) 
        


App = QApplication(sys.argv)
window2 = Window()
sys.exit(App.exec())