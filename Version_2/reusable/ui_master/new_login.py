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
from PyQt5.QtCore import * 
import sys 
from PyQt5.QtGui import *
import os
import datetime
import time
from PyQt5.QtCore import QTimer
import cv2
# import pygame
from PyQt5.QtCore import QTimer
from threading import Thread
import emoji
#####
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu
import sys




# Type a message

rec_sec=0
rec_min=0
move_smth=-381
zoom_smth=52


class Window(QMainWindow):
    last_used = ""
    
    def __init__(self):
        super().__init__()

        # with open("theme.txt") as file: # Use file to refer to the file object
        #     data = file.read()
        #     print (data)
            
        self.setFixedSize(1051, 560) 
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        uic.loadUi("Chat_box.ui", self) 
        self.setStyleSheet("QWidget { background-color: %s}" % QtGui.QColor(252, 255, 253).name())
        self.textedit_messegebox = self.findChild(QTextEdit, "messegebox_t")
        self.textedit_usersearch= self.findChild(QTextEdit, "user_search_t")
        # self.label = self.findChild(QLabel, "label")

        self.listWidget = self.findChild(QListWidget, "listWidget")
        self.label_6.setHidden(True)
        self.label_7.setHidden(True)

        self.send_b_6.clicked.connect(lambda: self.emoji_v(":rose:"))
        self.send_b_3.clicked.connect(lambda: self.emoji_v(":grimacing_face:"))
        self.send_b_2.clicked.connect(lambda: self.emoji_v(":folded_hands:"))
        self.send_b_5.clicked.connect(lambda: self.emoji_v(":flexed_biceps:"))
        self.send_b_4.clicked.connect(lambda: self.emoji_v(":waving_hand:"))

        self.send_b_10.clicked.connect(lambda: self.emoji_v(":thumbs_up:"))
        self.send_b_9.clicked.connect(lambda: self.emoji_v(":OK_hand:"))
        self.send_b_8.clicked.connect(lambda: self.emoji_v(":smiling_face_with_3_hearts:"))
        self.send_b_7.clicked.connect(lambda: self.emoji_v(":hand_with_fingers_splayed:"))
        self.send_b_12.clicked.connect(lambda: self.emoji_v(":kiss_mark:"))

        self.send_b_6.setStyleSheet("background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        self.send_b_3.setStyleSheet("background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        self.send_b_2.setStyleSheet("background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        self.send_b_5.setStyleSheet("background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        self.send_b_4.setStyleSheet("background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")

        self.send_b_10.setStyleSheet("background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        self.send_b_9.setStyleSheet("background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        self.send_b_8.setStyleSheet("background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        self.send_b_7.setStyleSheet("background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        self.send_b_12.setStyleSheet("background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        self.emoji_FRM.setStyleSheet("background-color: rgba(255, 255, 255, .7);border: 0px solid gray;font-size: 25px;border-radius:10px;")

        
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
        # self.label_bottomchatbar = self.findChild(QLabel, "bottomchat_bar_l")
        
        self.label_usernamem = self.findChild(QLabel, "usernamem_l")
        self.label_lastseen = self.findChild(QLabel, "lastseen_l")
        self.button_menu_user= self.findChild(QPushButton, "menu_user_b")
        self.button_searchuser= self.findChild(QPushButton, "searchuser_b")
        self.button_call= self.findChild(QPushButton, "call_b")


        self.label_background = self.findChild(QLabel, "background_l")
        self.label_background.setPixmap(QPixmap(os.path.abspath(os.getcwd()+'/icons/background.png')))
        
        # self.bottomchat_bar_l.setStyleSheet('background-color:rgba(240, 240, 240, 0.5);')

        self.doc_BTN.setStyleSheet("background-color: transparent;border: 0px solid transparent;")
        self.camera_BTN.setStyleSheet("background-color: transparent;border: 0px solid transparent;")
        self.pushButton.setStyleSheet("background-color: transparent;border: 0px solid transparent;")
        self.pushButton_2.setStyleSheet("background-color: transparent;border: 0px solid transparent;")


        self.button_menu_user.setStyleSheet("background-color: transparent;border: 1px solid transparent;") 
        self.button_searchuser.setStyleSheet("background-color: transparent;border: 1px transparent;")
        self.button_call.setStyleSheet("background-color: transparent;border: 1px transparent;")
        self.label_lastseen.setStyleSheet("background-color: transparent;border: 1px solid transparent;")
        self.label_usernamem.setStyleSheet("background-color: transparent;border: 1px solid transparent;")
       
        # self.label_bottomchatbar.setStyleSheet("QWidget { background-color: %s}" % QtGui.QColor(255, 255, 255).name())
        # self.label_topchatbar.setStyleSheet("QWidget { background-color: %s}" % QtGui.QColor(255, 255, 255).name())
        self.label_sidebar.setStyleSheet("QWidget { background-color: %s};border: 1px solid white;" % QtGui.QColor(1, 36, 32).name())
        # self.label_bottomchatbar.setStyleSheet("border: 1px solid lightgray;")
        # self.label_topchatbar.setStyleSheet("border: 1px solid lightgray;")
        
        self.button_menu.setStyleSheet("background-color: white;border: 1px solid white;border-radius:15px;")
        # self.emoji_BTN.setIcon
        self.emoji_BTN.setStyleSheet("background-color: transparent;border: 1px solid white;border-radius:15px;") 
        self.emoji_BTN_2.setStyleSheet("background-color: transparent;border: 1px solid white;border-radius:15px;") 

        self.clear_b.setWhatsThis("lksdaf;jksnf;j")


        self.label_5.setStyleSheet("background-color: transparent;")

        self.button_record.setStyleSheet("background-color: transparent;border: 1px solid white;border-radius:15px;") 
        self.button_send.setStyleSheet("background-color: transparent;border: 0px solid white;border-radius:15px;") 
        self.button_attach.setStyleSheet("background-color: transparent;border: 0px solid white;border-radius:15px;") 
        self.textedit_messegebox.setStyleSheet("background-color: white;border: 1px solid lightgray;border-radius:15px;font-size: 18px;") 
        self.button_usersearch.setStyleSheet("background-color: white;border: 1px solid white;") 
        self.textedit_usersearch.setStyleSheet("background-color: white;border: 1px solid gray;border-radius:15px;") 
        
        self.button_menu_user.setIcon(QIcon(os.getcwd()+'/icons/menu_user.png'))
        self.button_searchuser.setIcon(QIcon(os.getcwd()+'/icons/search.png'))
        self.button_call.setIcon(QIcon(os.getcwd()+'/icons/phone.png'))
        self.emoji_BTN_2.setIcon(QIcon(os.getcwd()+'/icons/laugh2.png'))
        self.emoji_BTN.setIcon(QIcon(os.path.abspath(os.getcwd() + '/icons/laugh.png')))

        self.button_usersearch.setIcon(QIcon(os.getcwd()+'/icons/search.png'))
        self.button_menu.setIcon(QIcon(os.getcwd()+'/icons/menu.png'))
        self.button_record.setIcon(QIcon(os.getcwd()+'/icons/radio.png'))
        self.button_attach.setIcon(QIcon(os.getcwd()+'/icons/clip.png')) 
        self.button_send.setIcon(QIcon(os.getcwd()+'/icons/send.png'))  

        self.button_send.clicked.connect(self.clickedBtn_send)
        self.button_other.clicked.connect(self.clickedBtn_other) 
        self.button_clear.clicked.connect(self.voice_mess_other) 
        self.searchuser_b.clicked.connect(self.click_search) 
        self.pushButton.clicked.connect(self.back_from_search) 
        self.doc_BTN.clicked.connect(self.openFileNameDialog) 
        self.attach_b_2.clicked.connect(self.click_attach_2) 
        self.camera_BTN.clicked.connect(self.click_camera_BTN) 
        self.menu_b.clicked.connect(self.start_menu)
        self.menu_bk_BTN.clicked.connect(self.menu_back)
        self.emoji_BTN.clicked.connect(self.start_emoji_box)
        self.emoji_BTN_2.clicked.connect(self.exit_emoji_box)
        
        


        
        
  

        self.button_user.clicked.connect(self.clickedBtn_user)   
        self.button_attach.clicked.connect(self.click_attach)
        self.textedit_messegebox.textChanged.connect(self.textChanged_messege_event)

        # self.pushButton.
        self.pushButton_2.setHidden(True)
       
        self.pushButton.setHidden(True)
        self.lineEdit.setHidden(True)

        
       
        
        self.button_record.setHidden(False)
        self.button_send.setHidden(True)
        self.listWidget.currentItemChanged.connect(self.show_user_messege)
        self.listWidget.setStyleSheet("background-color: white;border: 0px solid lightgray;border-radius: 5px;") 
        self.textedit_messegebox.setFocus()
        self.setting_FRM.setStyleSheet("background-color: black;border: 0px solid lightgray;border-radius: 5px;")

        # window.pushButton_7.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/error.png')))
        # window.label_18.setHidden(False)
        # window.label_18.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')
        # movie = QtGui.QMovie(os.getcwd() + '/UI/Login/images/loading2.gif')
        # window.label_18.setMovie(movie)
        # movie.start()
        self.label.setHidden(True)

        self.attach_b_2.setHidden(True)
        self.attach_b_2.setIcon(QIcon(os.path.abspath(os.getcwd() + '/icons/clip.png')))
        self.menu_bk_BTN.setIcon(QIcon(os.path.abspath(os.getcwd() + '/icons/arrow.png')))
        self.menu_bk_BTN.setStyleSheet("background-color: transparent;border: 0px solid white;border-radius:15px;") 


        self.scrollArea.verticalScrollBar().setStyleSheet("border: none;background: lightgray;height: 26px;margin: 0px 26px 0 26px;")
        

        self.profile_LBL.setPixmap(QPixmap(os.path.abspath(os.getcwd()+'/output.png')))
        self.profile_LBL.setStyleSheet("border: 0px solid gray ;border-radius: 90px;") 

        self.pv_LBL.setStyleSheet("background-color: transparent;border: 0px solid gray ;border-radius: 20px;") 
        self.pv_LBL.setIcon(QIcon(os.path.abspath(os.getcwd()+'/icons/pv.png')))
        self.label_7.setStyleSheet("background-color: transparent;") 
        self.label_6.setStyleSheet("background-color: transparent;") 
        self.emoji_FRM.setHidden(True)
        self.doc_BTN.setHidden(True)
        self.doc_BTN.setIcon(QIcon(os.path.abspath(os.getcwd() + '/icons/document.png')))

        self.camera_BTN.setHidden(True)
        self.camera_BTN.setIcon(QIcon(os.path.abspath(os.getcwd() + '/icons/camera.png')))

        self.record_b.setStyleSheet("background-color: transparent;border: 0px solid gray ;border-radius: 20px;") 
        self.record_b.setCheckable(True)
        self.record_b.toggle()
        self.record_b.clicked.connect(self.rec_voice)

        self.menu_user_b.clicked.connect(self.contex_menu)
        

        self.emoji_BTN_2.setEnabled(False)
        self.emoji_BTN_2.setHidden(True)
        



        # self.textedit_messegebox.setHidden(True)
        # self.label.setHidden(True)
        # self.label.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')

        # movie = QtGui.QMovie(os.getcwd() + '/icons/floding.gif')
        # print(os.getcwd() + '/icons/floading.gif')
        # self.label.setMovie(movie)
        # movie.start()
        # time.sleep(2)
        # movie.stop()

        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(lambda : movie.stop())
        # self.timer.singleShot(30)

        self.center()
        self.show()
    
    def emoji_v(self,from_f):
        self.messegebox_t.setText(self.messegebox_t.toPlainText()+emoji.emojize(from_f))
       
    def scrol_down(self):
        self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
        
    def wheelEvent(self,event):
        # if (self.scrollArea.verticalScrollBar().value==self.scrollArea.verticalScrollBar().maximum())
        print("d")
        pass
   
   
    def move_down(self):
        global move_smth,zoom_smth
        self.setting_FRM.setGeometry(QtCore.QRect(move_smth, 0, 381, 581))
        move_smth-=3
        zoom_smth-=1
        self.profile_LBL.resize(zoom_smth, zoom_smth)
        self.profile_LBL.setStyleSheet("border: 0px solid gray ;border-radius: %dpx;"% int(zoom_smth/2))
        if move_smth ==-384:
            self.timer.stop()
            # move_smth=0
   
    def rec_sec(self):
        global rec_sec
        global rec_min
        rec_sec+=1
        
        if rec_sec==60:
            rec_min+=1
            rec_sec=0
        self.label_6.setText("%02d:%02d"%(rec_min,rec_sec))
        self.label_6.setStyleSheet("background-color: transparent;border: 0px solid transparent;font-size: 20px;")


    def rec_voice(self):
        self.exit_emoji_box()
        if self.record_b.isChecked():
            global rec_min
            global rec_sec
            rec_min = 0
            rec_sec=0
            self.timer.stop() 
            self.record_b.setIcon(QIcon(QPixmap(os.path.abspath(os.getcwd() + '/icons/radio.png'))))
            self.emoji_BTN.setEnabled(True)
            self.messegebox_t.setEnabled(True)
            self.label_6.setHidden(True)
            self.label_7.setHidden(True)
            self.messegebox_t.resize(571, 31)
            movie = QtGui.QMovie(os.getcwd() + '/icons/rec_button.gif')
            self.label_7.setMovie(movie)
            movie.stop()
            print ("button pressed")
        else:
            self.label_6.setText("00:00")
            self.label_6.setStyleSheet("background-color: transparent;border: 0px solid transparent;font-size: 20px;")
            self.emoji_BTN.setEnabled(False)
            self.messegebox_t.setEnabled(False)
            self.label_6.setHidden(False)
            self.label_7.setHidden(False)
            self.messegebox_t.resize(461, 31)
            movie = QtGui.QMovie(os.getcwd() + '/icons/rec_button.gif')
            self.label_7.setMovie(movie)
            movie.start()
            self.record_b.setIcon(QIcon(QPixmap(os.path.abspath(os.getcwd() + '/icons/mic_send.png'))))
            print ("button released")
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.rec_sec)
            self.timer.start(1000) 

           
    def contex_menu(self):
        menu = QMenu(self)
        info=newAct = menu.addAction("info")
        mute=menu.addAction("mute")
        clear_messages=menu.addAction("clear messages")
        Delete_Chat=menu.addAction("Delete Chat")
        info.triggered.connect(lambda:print("d0"))
        mute.triggered.connect(lambda:print("d1"))
        clear_messages.triggered.connect(lambda:print("d2"))
        Delete_Chat.triggered.connect(lambda:print("d3"))
        menu.exec_(QCursor.pos())
        
        

    def menu_back(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.move_down)
        self.timer.start(1)        



    def move_ups(self):
        global move_smth,zoom_smth
        self.setting_FRM.setGeometry(QtCore.QRect(move_smth, 0, 381, 581))
        move_smth+=3
        zoom_smth+=1
        self.profile_LBL.resize(zoom_smth, zoom_smth)
        self.profile_LBL.setStyleSheet("border: 0px solid gray ;border-radius: %dpx;"% int(zoom_smth/2))
        if move_smth ==3:
            self.timer.stop()
    



    def start_menu(self):
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.move_ups)
        self.timer.start(1)


    
    def start_emoji_box(self):
        self.emoji_FRM.setHidden(False)

        self.emoji_BTN.setEnabled(False)
        self.emoji_BTN.setHidden(True)
        self.emoji_BTN_2.setEnabled(True)
        self.emoji_BTN_2.setHidden(False)
            

    def exit_emoji_box(self):
        self.emoji_FRM.setHidden(True)


        self.emoji_BTN.setEnabled(True)
        self.emoji_BTN.setHidden(False)
        self.emoji_BTN_2.setEnabled(False)
        self.emoji_BTN_2.setHidden(True)
        

    def click_camera_BTN(self):
        cv2.namedWindow("preview")
        vc = cv2.VideoCapture(0)

        if vc.isOpened(): # try to get the first frame
            rval, frame = vc.read()
        else:
            rval = False

        while rval:
            cv2.imshow("preview", frame)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27: # exit on ESC
                break
        cv2.destroyWindow("preview")        


    def click_attach(self):
        # if self.camera_BTN.setHidden(False):#:\\\\\\\\\\\\\\\\\\\\\\\
        #     self.camera_BTN.setHidden(True)
        #     self.doc_BTN.setHidden(True)            

        # else:
        self.attach_b.setHidden(True)
        self.attach_b_2.setHidden(False)
        self.camera_BTN.setHidden(False)
        self.doc_BTN.setHidden(False)



    def click_attach_2(self):
        self.attach_b.setHidden(False)
        self.attach_b_2.setHidden(True)
        self.camera_BTN.setHidden(True)
        self.doc_BTN.setHidden(True)        


    def click_search(self):
        self.attach_b.setEnabled(False)
        self.messegebox_t.setEnabled(False)
        self.emoji_BTN.setEnabled(False)
        self.record_b.setEnabled(False)
        self.pv_LBL.setHidden(True)
        self.searchuser_b.setHidden(True)
        
        

        self.click_attach_2()
        self.label.setHidden(False)
        self.label.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')


        self.button_call.setHidden(True)
        self.menu_user_b.setHidden(True)
        self.usernamem_l.setHidden(True)
        self.lastseen_l.setHidden(True)


        # self.searchuser_b.setGeometry(QtCore.QRect(1010, 10, 31, 31))
        self.pushButton_2.setHidden(False)
        self.pushButton_2.setIcon(QIcon(os.path.abspath(os.getcwd() + '/icons/search.png')))

        self.pushButton.setHidden(False)
        self.pushButton.setIcon(QIcon(os.path.abspath(os.getcwd() + '/icons/back.png')))

        self.lineEdit.setHidden(False)
        self.lineEdit.setFocus()
        self.lineEdit.setStyleSheet("background-color: white;border: 1px solid lightgray;border-radius:15px;") 



    def back_from_search(self):
        self.attach_b.setEnabled(True)
        self.messegebox_t.setEnabled(True)
        self.record_b.setEnabled(True)
        self.emoji_BTN.setEnabled(True  )
        self.pv_LBL.setHidden(False)
        self.searchuser_b.setHidden(False)





        self.label.setHidden(True)



        self.button_call.setHidden(False)
        self.menu_user_b.setHidden(False)
        self.usernamem_l.setHidden(False)
        self.lastseen_l.setHidden(False)
        self.pushButton_2.setHidden(True)


        self.pushButton.setHidden(True)
        self.lineEdit.setHidden(True)
        self.searchuser_b.setGeometry(QtCore.QRect(930, 10, 31, 31))


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"FileDialog", "","All Files ();;Python Files (.py)", options=options)
        if fileName:
            print(fileName)
    

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            # self.close()
            self.clickedBtn_send()

        # if event.key() == Qt.Key_2:
        #     # self.clickedBtn_send()
        #     # self.textedit_messegebox.textChanged("gggggggggg")
        #     # self.textedit_messegebox.setfocus()
        #     pass


    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

   
    def show_user_messege(self):
        self.clear_screen()


    def clickedBtn_send(self):
        self.exit_emoji_box()
        if self.scrollArea.verticalScrollBar().value()==self.scrollArea.verticalScrollBar().maximum():
            QTimer.singleShot(50, self.scrol_down)
        if self.textedit_messegebox.toPlainText().strip() :
            massege_text="\n   "
            self.user_image = QPushButton()
            self.user_image.setIcon(QIcon(os.path.abspath(os.getcwd()+'/icons/me.png')))
            self.user_image.setIconSize(QSize(35,35))
        
            if len(self.textedit_messegebox.toPlainText())<=66:
                self.messege_user = QLabel("  " + self.textedit_messegebox.toPlainText(),self)
            else:    
                i=0
                while(len(massege_text)-8<=len(self.textedit_messegebox.toPlainText())):
                    
                    massege_text=massege_text+self.textedit_messegebox.toPlainText()[i:i+66]+"\n   "
                    i=66+i
                self.messege_user = QLabel(massege_text,self)

                

            
            
            self.messege_user.setStyleSheet("background-color: #D7FAB3;border: 0px solid lightgray;border-radius: 17px;font-size: 20px;") 
            if self.last_used == "other" :
                self.formLayout.addRow(QLabel())
                
            self.textedit_messegebox.clear()
            self.formLayout.addRow(self.user_image,self.messege_user)

            self.formLayout.itemAt(self.formLayout.count()-2).widget().clicked.connect(self.clickedBtn_user)
            self.formLayout.itemAt(self.formLayout.count()-2).widget().setStyleSheet(
                "background-color:transparent;border: 0px solid white;border-radius:20px;color:white;")
            self.formLayout.itemAt(self.formLayout.count()-2).widget().setCursor(QCursor(QtCore.Qt.PointingHandCursor))


            self.messege_time = QLabel(" 12:54 ",alignment=Qt.AlignRight)
            self.messege_time.setStyleSheet("color: black")
            self.messege_time.setStyleSheet("background-color: white;border: 0px solid lightgray;border-radius: 5px;font-size: 14px;") 
            self.seen_image = QLabel()
            self.seen_image.setPixmap(QPixmap(os.path.abspath(os.getcwd()+'/icons/not_seen.png')).scaledToWidth(20))
            self.formLayout.addRow(self.messege_time,self.seen_image)
            self.last_used="me"


    def clickedBtn_other(self):
        
        if self.scrollArea.verticalScrollBar().value()==self.scrollArea.verticalScrollBar().maximum():
            QTimer.singleShot(50, self.scrol_down)
        self.user_image = QPushButton()
        self.user_image.setIcon(QIcon(os.path.abspath(os.getcwd()+'/icons/user.png')))
        self.user_image.setIconSize(QSize(35,35))
        # self.user_image.setPixmap(QPixmap(os.path.abspath(os.getcwd()+'/icons/user.png')).scaledToWidth(35))
        self.messege_user = QLabel(" slm mmd")
        self.messege_user.setStyleSheet("background-color: white;border: 1px solid lightgray;border-radius: 17px;font-size: 20px;")
        if self.last_used == "me" :
            self.formLayout.addRow(QLabel())  
        self.formLayout.addRow(self.user_image,self.messege_user)
        self.formLayout.itemAt(self.formLayout.count()-2).widget().clicked.connect(self.clickedBtn_user)

        self.formLayout.itemAt(self.formLayout.count()-2).widget().setStyleSheet(
            "background-color:transparent;border: 0px solid white;border-radius:20px;color:white;")
        self.formLayout.itemAt(self.formLayout.count()-2).widget().setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        
        self.messege_time = QLabel(datetime.datetime.now().strftime("%H:%M"),alignment=Qt.AlignRight)
        self.messege_time.setStyleSheet("color: black")
        self.messege_time.setStyleSheet("background-color: transparent;border: 0px solid lightgray;border-radius: 5px;font-size: 14px;") 
        self.seen_image = QPushButton()
        # self.seen_image.setIcon(QIcon(os.path.abspath(os.getcwd()+'/icons/reply.png')))
        self.seen_image.setStyleSheet("background-color: transparent;border: 0px solid white;border-radius: 10px;") 
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight)
        self.formLayout.addRow(self.seen_image,self.messege_time)
        self.last_used="other"
        





    def voice_mess_other(self):
        self.formLayout.addRow(QLabel())
        if self.scrollArea.verticalScrollBar().value()==self.scrollArea.verticalScrollBar().maximum():
            QTimer.singleShot(50, self.scrol_down)
        self.user_image = QPushButton()
        self.user_image.setIcon(QIcon(os.path.abspath(os.getcwd()+'/icons/user.png')))
        self.user_image.setIconSize(QSize(35,35))
        if self.last_used == "me" :
            self.formLayout.addRow(QLabel())
        self.seen_image = QPushButton()
        self.seen_image.setIcon(QIcon(os.path.abspath(os.getcwd()+'/icons/google-play.png')))
        self.seen_image.setStyleSheet("background-color: white;border: 3px solid white;border-radius: 10px;")   
        
        self.formLayout.addRow(self.user_image,self.seen_image)
        self.formLayout.itemAt(self.formLayout.count()-2).widget().clicked.connect(self.clickedBtn_user)
        self.formLayout.itemAt(self.formLayout.count()-2).widget().setStyleSheet(
            "background-color:transparent;border: 0px solid white;border-radius:20px;color:white;")

            
        self.formLayout.itemAt(self.formLayout.count()-2).widget().setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.formLayout.itemAt(self.formLayout.count()-1).widget().clicked.connect(self.clickedBtn_user)
        

            
        self.formLayout.itemAt(self.formLayout.count()-1).widget().setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        
        



    
        self.messege_time = QLabel(datetime.datetime.now().strftime("%H:%M"),alignment=Qt.AlignRight)
        self.messege_time.setStyleSheet("color: black")
        self.messege_time.setStyleSheet("background-color: transparent;border: 0px solid lightgray;border-radius: 5px;font-size: 14px;") 
        
        self.voice = QSlider(Qt.Horizontal)

        self.voice.setMinimum(10)
        self.voice.setMaximum(30)
        ##
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight)
        self.formLayout.addRow(self.messege_time,self.voice)
        self.formLayout.itemAt(self.formLayout.count()-1).widget().sliderReleased.connect(self.clickedBtn_user)
        
        self.formLayout.addRow(QLabel())
        self.formLayout.addRow(QLabel())
        self.last_used="other"


    def voice_mess_me(self):
        pass
  
  
    def clickedBtn_user(self):
        # self.formLayout.QPushButton.click()
        itm = QListWidgetItem( "\n   Mohammad Hossein Fadavi\n " )
        itm.setIcon(QIcon(os.path.abspath(os.getcwd()+'/icons/user.png')))
        self.listWidget.addItem(itm)
        
        # self.listWidget.item(1).setForeground(QtCore.Qt.blue)
        
       
    def textChanged_messege_event(self):
        
        if self.textedit_messegebox.toPlainText().strip() :
            self.button_record.setHidden(True)
            self.button_send.setHidden(False)
        else:
            self.button_record.setHidden(False)
            self.button_send.setHidden(True)

        
    def clear_screen(self):
        # find text in form layout
        # for i in range(int(self.formLayout.count()/4)): 
        #     print(self.formLayout.itemAt(i*4+1).widget().text())
        
        
        # clear text 
        for i in reversed(range(self.formLayout.count())): 
            self.formLayout.itemAt(i).widget().deleteLater()
        # pass


App = QApplication(sys.argv)
window2 = Window()
sys.exit(App.exec())