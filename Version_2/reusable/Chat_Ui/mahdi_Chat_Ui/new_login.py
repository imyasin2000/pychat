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

        self.listWidget = self.findChild(QListWidget, "listWidget")
        

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
        self.button_clear.clicked.connect(self.clear_screen) 
        self.searchuser_b.clicked.connect(self.click_search) 
        self.pushButton.clicked.connect(self.back_from_search) 
        self.doc_BTN.clicked.connect(self.openFileNameDialog) 
        self.attach_b_2.clicked.connect(self.click_attach_2) 
        self.camera_BTN.clicked.connect(self.click_camera_BTN) 
        
        
  

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


        # window.pushButton_7.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/error.png')))
        # window.label_18.setHidden(False)
        # window.label_18.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')
        # movie = QtGui.QMovie(os.getcwd() + '/UI/Login/images/loading2.gif')
        # window.label_18.setMovie(movie)
        # movie.start()
        self.label.setHidden(True)

        self.attach_b_2.setHidden(True)
        self.attach_b_2.setIcon(QIcon(os.path.abspath(os.getcwd() + '/icons/clip.png')))

        

        self.doc_BTN.setHidden(True)
        self.doc_BTN.setIcon(QIcon(os.path.abspath(os.getcwd() + '/icons/document.png')))

        self.camera_BTN.setHidden(True)
        self.camera_BTN.setIcon(QIcon(os.path.abspath(os.getcwd() + '/icons/camera.png')))


        # self.textedit_messegebox.setHidden(True)


        self.center()
        self.show()

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







    # def click_doc_BTN(self):




    def click_search(self):
        self.attach_b.setEnabled(False)
        self.messegebox_t.setEnabled(False)
        self.record_b.setEnabled(False)

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


        self.label.setHidden(True)



        self.button_call.setHidden(False)
        self.menu_user_b.setHidden(False)
        self.usernamem_l.setHidden(False)
        self.lastseen_l.setHidden(False)
        self.pushButton_2.setHidden(True)


        self.pushButton.setHidden(True)
        self.lineEdit.setHidden(True)
        self.searchuser_b.setGeometry(QtCore.QRect(970, 10, 31, 31))






    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"FileDialog", "","All Files (*);;Python Files (*.py)", options=options)
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
        self.messege_user = QLabel(" slm mmd")
        self.messege_user.setStyleSheet("background-color: white;border: 1px solid lightgray;border-radius: 17px;")

        
        if self.last_used == "me" :
            self.formLayout.addRow(QLabel())
            
        self.formLayout.addRow(self.user_image,self.messege_user)
        self.messege_time = QLabel(datetime.datetime.now().strftime("%H:%M"),alignment=Qt.AlignRight)
        self.messege_time.setStyleSheet("color: black")
        self.messege_time.setStyleSheet("background-color: transparent;border: 0px solid lightgray;border-radius: 5px;") 
        self.seen_image = QPushButton()
        self.seen_image.setIcon(QIcon(os.path.abspath(os.getcwd()+'/icons/reply.png')))
        self.seen_image.setStyleSheet("background-color: transparent;border: 3px solid white;border-radius: 10px;") 
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight)
        self.formLayout.addRow(self.seen_image,self.messege_time)
        self.last_used="other"

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