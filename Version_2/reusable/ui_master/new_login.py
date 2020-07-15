import pyaudio
import wave
import threading

from PyQt5.QtWidgets import *  # UI
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
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu,QMessageBox
import sys
from PIL import Image, ImageOps, ImageDraw


from playsound import playsound #++sudo apt-get install ffmpeg
import os
import shutil
from pydub.utils import mediainfo





# Type a message

record_until = True
rec_sec = 0
rec_min = 0
play_sec=-1
move_smth = -381
zoom_smth = 52
zoom_smth2 = 0
zoom_smth3 = 0
move_smth1 = 550
move_smth2 = 571
mic_port=True

class Window(QMainWindow):
    last_used = ""

    def __init__(self):
        super().__init__()

        # with open("theme.txt") as file: # Use file to refer to the file object
        #     data = file.read()
        #     print (data)

        self.setFixedSize(1051, 560)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint |
                            QtCore.Qt.WindowMinimizeButtonHint)
        uic.loadUi("Chat_box.ui", self)
        self.setStyleSheet("QWidget { background-color: %s}" %
                           QtGui.QColor(252, 255, 253).name())
        self.textedit_messegebox = self.findChild(QTextEdit, "messegebox_t")
        self.textedit_usersearch = self.findChild(QTextEdit, "user_search_t")
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
        self.send_b_8.clicked.connect(
            lambda: self.emoji_v(":smiling_face_with_3_hearts:"))
        self.send_b_7.clicked.connect(
            lambda: self.emoji_v(":hand_with_fingers_splayed:"))
        self.send_b_12.clicked.connect(lambda: self.emoji_v(":kiss_mark:"))

        self.send_b_6.setStyleSheet(
            "background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
       
        self.label.setStyleSheet("background-color: white;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        self.label_10.setStyleSheet("background-color: white;border: 0px solid gray;border-radius:10px;color:rgb(0, 193, 165);font-size: 15px;")
        self.label_13.setStyleSheet("background-color: white;border: 0px solid gray;border-radius:10px;color:rgb(0, 193, 165);font-size: 15px;")
        self.label_11.setStyleSheet("background-color: white;border: 0px solid gray;border-radius:10px;color:rgb(0, 0, 0);font-size: 13px;")
        self.label_12.setStyleSheet("background-color: white;border: 0px solid gray;border-radius:10px;color:rgb(0, 0, 0);font-size: 13px;")
        
        self.line.setStyleSheet("background-color: rgb(240, 240, 240);")
        



        self.send_b_3.setStyleSheet(
            "background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        self.send_b_2.setStyleSheet(
            "background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        self.send_b_5.setStyleSheet(
            "background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        self.send_b_4.setStyleSheet(
            "background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")

        self.send_b_10.setStyleSheet(
            "background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        self.send_b_9.setStyleSheet(
            "background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        self.send_b_8.setStyleSheet(
            "background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        self.send_b_7.setStyleSheet(
            "background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        self.send_b_12.setStyleSheet(
            "background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        self.emoji_FRM.setStyleSheet(
            "background-color: rgba(255, 255, 255, .7);border: 0px solid gray;font-size: 25px;border-radius:10px;")

        self.button_user = self.findChild(QPushButton, "user_b")
        self.button_send = self.findChild(QPushButton, "send_b")
        self.button_other = self.findChild(QPushButton, "other_b")
        self.button_clear = self.findChild(QPushButton, "clear_b")
        self.button_attach = self.findChild(QPushButton, "attach_b")
        self.button_record = self.findChild(QPushButton, "record_b")
        self.button_menu = self.findChild(QPushButton, "menu_b")
        self.button_usersearch = self.findChild(QPushButton, "user_search_b")
        self.label_sidebar = self.findChild(QLabel, "side_bar_l")
        # self.label_topchatbar = self.findChild(QLabel, "topchat_bar_l")
        # self.label_bottomchatbar = self.findChild(QLabel, "bottomchat_bar_l")

        self.label_usernamem = self.findChild(QLabel, "usernamem_l")
        self.label_lastseen = self.findChild(QLabel, "lastseen_l")
        self.button_menu_user = self.findChild(QPushButton, "menu_user_b")
        self.button_searchuser = self.findChild(QPushButton, "searchuser_b")
        self.button_call = self.findChild(QPushButton, "call_b")

        self.label_background = self.findChild(QLabel, "background_l")
        self.label_background.setPixmap(
            QPixmap(os.path.abspath(os.getcwd()+'/icons/background.png')))

        # self.bottomchat_bar_l.setStyleSheet('background-color:rgba(240, 240, 240, 0.5);')

        self.doc_BTN.setStyleSheet(
            "background-color: transparent;border: 0px solid transparent;")
        self.camera_BTN.setStyleSheet(
            "background-color: transparent;border: 0px solid transparent;")
        self.pushButton.setStyleSheet(
            "background-color: transparent;border: 0px solid transparent;")
        self.pushButton_2.setStyleSheet(
            "background-color: transparent;border: 0px solid transparent;")

        self.button_menu_user.setStyleSheet(
            "background-color: transparent;border: 1px solid transparent;")
        self.button_searchuser.setStyleSheet(
            "background-color: transparent;border: 1px transparent;")
        self.button_call.setStyleSheet(
            "background-color: transparent;border: 1px transparent;")
        self.label_lastseen.setStyleSheet(
            "background-color: transparent;border: 1px solid transparent;")
        self.label_usernamem.setStyleSheet(
            "background-color: transparent;border: 1px solid transparent;")

        # self.label_bottomchatbar.setStyleSheet("QWidget { background-color: %s}" % QtGui.QColor(255, 255, 255).name())
        # self.label_topchatbar.setStyleSheet("QWidget { background-color: %s}" % QtGui.QColor(255, 255, 255).name())
        self.label_sidebar.setStyleSheet(
            "QWidget { background-color: %s};border: 1px solid white;" % QtGui.QColor(1, 36, 32).name())
        # self.label_bottomchatbar.setStyleSheet("border: 1px solid lightgray;")
        # self.label_topchatbar.setStyleSheet("border: 1px solid lightgray;")

        self.button_menu.setStyleSheet(
            "background-color: white;border: 1px solid white;border-radius:15px;")
        # self.emoji_BTN.setIcon
        self.emoji_BTN.setStyleSheet(
            "background-color: transparent;border: 1px solid white;border-radius:15px;")
        self.emoji_BTN_2.setStyleSheet(
            "background-color: transparent;border: 1px solid white;border-radius:15px;")

        self.clear_b.setWhatsThis("lksdaf;jksnf;j")

        self.label_5.setStyleSheet("background-color: transparent;")

        self.button_record.setStyleSheet(
            "background-color: transparent;border: 1px solid white;border-radius:15px;")
        self.button_send.setStyleSheet(
            "background-color: transparent;border: 0px solid white;border-radius:15px;")

        self.send_b_11.setStyleSheet(
            "background-color: light gray;border: 0px solid white;border-radius:20px;")

        self.send_b_11.setIcon(QIcon(os.getcwd()+'/icons/up-chevron.png'))
        self.send_b_11.setHidden(True)
        self.button_attach.setStyleSheet(
            "background-color: transparent;border: 0px solid white;border-radius:15px;")
        self.textedit_messegebox.setStyleSheet(
            "background-color: white;border: 1px solid lightgray;border-radius:18px;font-size: 20px;")
        self.button_usersearch.setStyleSheet(
            "background-color: white;border: 1px solid white;")
        self.textedit_usersearch.setStyleSheet(
            "background-color: white;border: 1px solid gray;border-radius:15px;")

        self.button_menu_user.setIcon(
            QIcon(os.getcwd()+'/icons/menu_user.png'))
        self.button_searchuser.setIcon(QIcon(os.getcwd()+'/icons/search.png'))
        self.button_call.setIcon(QIcon(os.getcwd()+'/icons/phone.png'))
        self.emoji_BTN_2.setIcon(QIcon(os.getcwd()+'/icons/laugh2.png'))
        self.emoji_BTN.setIcon(
            QIcon(os.path.abspath(os.getcwd() + '/icons/laugh.png')))

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

        self.clear_b_2.clicked.connect(self.file_receve)

        self.menu_bk_BTN.clicked.connect(self.menu_back)
        self.emoji_BTN.clicked.connect(self.start_emoji_box)
        self.emoji_BTN_2.clicked.connect(self.exit_emoji_box)

        self.send_b_11.clicked.connect(self.scrol_down)

        self.scrollArea.setMouseTracking(True)

        # self.label_3.mouseReleaseEvent = self.clickedBtn_other()

        self.button_user.clicked.connect(self.clickedBtn_user)
        self.button_attach.clicked.connect(self.click_attach)
        self.textedit_messegebox.textChanged.connect(
            self.textChanged_messege_event)

        # self.pushButton.
        self.pushButton_2.setHidden(True)

        self.pushButton.setHidden(True)
        self.lineEdit.setHidden(True)

        self.button_record.setHidden(False)
        self.button_send.setHidden(True)
        self.listWidget.itemClicked.connect(self.user_list_click)
        self.listWidget.setStyleSheet(
            "background-color: white;border: 0px solid lightgray;border-radius: 5px;")
        self.textedit_messegebox.setFocus()
        self.setting_FRM.setStyleSheet(
            "background-color: black;border: 0px solid lightgray;border-radius: 5px;")

        # window.pushButton_7.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/error.png')))
        # window.label_18.setHidden(False)
        # window.label_18.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')
        # movie = QtGui.QMovie(os.getcwd() + '/UI/Login/images/loading2.gif')
        # window.label_18.setMovie(movie)
        # movie.start()

        self.attach_b_2.setHidden(True)
        self.attach_b_2.setIcon(
            QIcon(os.path.abspath(os.getcwd() + '/icons/clip.png')))
        self.menu_bk_BTN.setIcon(
            QIcon(os.path.abspath(os.getcwd() + '/icons/arrow.png')))
        self.menu_bk_BTN.setStyleSheet(
            "background-color: transparent;border: 0px solid white;border-radius:15px;")

        self.scrollArea.verticalScrollBar().setStyleSheet(
            "border: none;background: lightgray;height: 26px;margin: 0px 26px 0 26px;")
        self.listWidget.verticalScrollBar().setStyleSheet(
            "border: none;background: lightgray;height: 26px;margin: 0px 26px 0 26px;")

        self.profile_LBL.setIcon(QIcon(os.path.abspath(os.getcwd() + '/Files/profile/output.png')))
        self.profile_LBL.clicked.connect(self.contex_change_profile)

        self.profile_LBL.setStyleSheet("border: 0px solid gray ;border-radius: 90px;")

        self.pv_LBL.setStyleSheet(
            "background-color: transparent;border: 0px solid gray ;border-radius: 20px;")
        self.pv_LBL.setIcon(
            QIcon(os.path.abspath(os.getcwd()+'/icons/pv.png')))
        self.label_7.setStyleSheet("background-color: transparent;")
        self.label_6.setStyleSheet("background-color: transparent;")
        # self.emoji_FRM.setHidden(True)
        self.doc_BTN.setHidden(True)
        self.doc_BTN.setIcon(QIcon(os.path.abspath(
            os.getcwd() + '/icons/document.png')))

        self.camera_BTN.setHidden(True)
        self.camera_BTN.setIcon(
            QIcon(os.path.abspath(os.getcwd() + '/icons/camera.png')))

        self.record_b.setStyleSheet(
            "background-color: transparent;border: 0px solid gray ;border-radius: 20px;")
        self.record_b.setIcon(
            QIcon(QPixmap(os.path.abspath(os.getcwd() + '/icons/radio.png'))))

        self.send_b_13.setStyleSheet(
            "background-color: transparent;border: 0px solid gray ;border-radius: 20px;")
        self.send_b_13.setIcon(
            QIcon(QPixmap(os.path.abspath(os.getcwd() + '/icons/close (1).png'))))
        self.send_b_13.setHidden(True)
        self.send_b_13.clicked.connect(self.stop_rec)
        self.call_b.clicked.connect(lambda : QMessageBox.about(self, "do not worry", "The ability to make calls will be added soon !!"))

        self.record_b.setCheckable(True)
        self.record_b.toggle()
        self.record_b.clicked.connect(self.rec_voice)
        self.record_b.setToolTip("<font color=white>%s</font>" % 'Voice Messege'.replace("\n", "<br/>"))
        self.send_b_13.setToolTip("<font color=white>%s</font>" % 'Delete Voice'.replace("\n", "<br/>"))
        self.emoji_BTN_2.setToolTip("<font color=white>%s</font>" % 'Close Emoji box'.replace("\n", "<br/>"))
        self.emoji_BTN.setToolTip("<font color=white>%s</font>" % 'Open Emoji box'.replace("\n", "<br/>"))
        self.doc_BTN.setToolTip("<font color=white>%s</font>" % 'Attach file'.replace("\n", "<br/>"))
        self.camera_BTN.setToolTip("<font color=white>%s</font>" % 'Take Picture'.replace("\n", "<br/>"))
        self.call_b.setToolTip("<font color=white>%s</font>" % 'Make Call'.replace("\n", "<br/>"))
        self.attach_b.setToolTip("<font color=white>%s</font>" % 'Attach'.replace("\n", "<br/>"))
        self.attach_b_2.setToolTip("<font color=black>%s</font>" % 'Attach'.replace("\n", "<br/>"))
        self.menu_user_b.setToolTip("<font color=white>%s</font>" % 'Menu'.replace("\n", "<br/>"))
        self.searchuser_b.setToolTip("<font color=white>%s</font>" % 'Search'.replace("\n", "<br/>"))
        self.send_b_11.setToolTip("<font color=black>%s</font>" % 'Scroll Down'.replace("\n", "<br/>"))
        self.send_b.setToolTip("<font color=white>%s</font>" % 'Send'.replace("\n", "<br/>"))
        self.pv_LBL.setToolTip("<font color=white>%s</font>" % 'Profile'.replace("\n", "<br/>"))
        self.pushButton_2.setToolTip("<font color=white>%s</font>" % 'Search'.replace("\n", "<br/>"))
        self.pushButton.setToolTip("<font color=white>%s</font>" % 'Cancel Search'.replace("\n", "<br/>"))
        self.user_search_b.setToolTip("<font color=black>%s</font>" % 'Search'.replace("\n", "<br/>"))
        self.menu_b.setToolTip("<font color=black>%s</font>" % 'Menu'.replace("\n", "<br/>"))
        self.menu_bk_BTN.setToolTip("<font color=white>%s</font>" % 'Go Back'.replace("\n", "<br/>"))

        
        
        
        
        
        
        
        

        self.menu_user_b.clicked.connect(self.contex_menu)

        self.emoji_BTN_2.setEnabled(True)
        self.emoji_BTN_2.setHidden(True)

        self.emoji_FRM.setHidden(True)
        self.label_8.setHidden(True)
        self.label_9.setHidden(True)

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
        self.timer10 = QtCore.QTimer()
        self.timer10.timeout.connect(self.move_down_wheel)
        self.timer10.start(500)
        self.center()

        
        self.show()



    def user_list_click(self,item):
        print(item.whatsThis())
 
    def contex_change_profile(self):
        menu = QMenu(self)
        View = newAct = menu.addAction("View photo")
        Take = menu.addAction("Take photo")
        Upload = menu.addAction("Upload photo")
        Remove = menu.addAction("Remove photo")

        View.triggered.connect(self.show_profile_pic)
        Take.triggered.connect(self.capture_pic_profile)
        Upload.triggered.connect(self.choose_profile_pic)
        Remove.triggered.connect(self.delete_profile_pic)
        menu.exec_(QCursor.pos())
    
    def delete_profile_pic(self):
        qm = QMessageBox()
        ret = qm.question(self,'warning!', "Are you sure you want to delete your profile picture?", qm.Yes | qm.No)
        if ret == qm.Yes:
            src = os.path.abspath(os.getcwd() + '/icons/output.png')
            dst = os.path.abspath(os.getcwd() + '/Files/profile/output.png')
            shutil.copy(src, dst)
            self.profile_LBL.setIcon(QIcon(os.path.abspath(os.getcwd() + '/Files/profile/output.png')))
        else:
            pass
        
    def show_profile_pic(self):
        

        img = Image.open(os.path.abspath(os.getcwd() + '/Files/profile/output.png'))
        defult = Image.open(os.path.abspath(os.getcwd() + '/icons/output.png'))

        if defult.histogram() == img.histogram(): 
            QMessageBox.about(self, "PyChat", "You do not have a profile picture to display")
            
        else:
            img.show()
            

    

    def choose_profile_pic(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.png)")
        dst = os.path.abspath(os.getcwd() + '/Files/profile/output.png')
       
        shutil.copy(fname[0], dst)
        #circle pic
        size = (500, 500)
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + size, fill=255)
        from PIL import ImageFilter
        im = Image.open(os.path.abspath(os.getcwd()+'/Files/profile/output.png'))
        output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)
        output.save(os.path.abspath(os.getcwd()+'/Files/profile/output.png'))

        self.profile_LBL.setIcon(QIcon(os.path.abspath(os.getcwd() + '/Files/profile/output.png')))
        
    def capture_pic_profile(self):
        QMessageBox.about(self, "Hint", "press space to capture picture or esc to quit")
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("Profile Pic")
        while True:
            ret, frame = cam.read()
            if not ret:
                break
            cv2.imshow("Profile Pic", frame)
            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = os.path.abspath(os.getcwd() + '/Files/profile/output.png')
                cv2.imwrite(img_name, frame)
                
                #circle pic
                size = (500, 500)
                mask = Image.new('L', size, 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0) + size, fill=255)
                from PIL import ImageFilter
                im = Image.open(os.path.abspath(os.getcwd()+'/Files/profile/output.png'))
                output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
                output.putalpha(mask)
                output.save(os.path.abspath(os.getcwd()+'/Files/profile/output.png'))
                cam.release()
                cv2.destroyAllWindows()
                self.profile_LBL.setIcon(QIcon(os.path.abspath(os.getcwd() + '/Files/profile/output.png')))


               

        cam.release()

        cv2.destroyAllWindows()

    def file_receve(self):
        if self.scrollArea.verticalScrollBar().value() == self.scrollArea.verticalScrollBar().maximum():
            QTimer.singleShot(50, self.scrol_down)
        self.user_image = QPushButton()
        self.user_image.setIcon(
            QIcon(os.path.abspath(os.getcwd()+'/icons/user.png')))
        self.user_image.setIconSize(QSize(35, 35))

        self.messege_user = QPushButton()
        self.messege_user.setIcon(
            QIcon(os.path.abspath(os.getcwd()+'/icons/download.png')))
        self.messege_user.setIconSize(QSize(400, 300))

        # self.messege_user.setStyleSheet("background-color: white;border: 1px solid lightgray;border-radius: 17px;font-size: 20px;")
        if self.last_used == "me":
            self.formLayout.addRow(QLabel())
        self.formLayout.addRow(self.user_image, self.messege_user)
        self.formLayout.itemAt(self.formLayout.count()-2).widget().clicked.connect(self.clickedBtn_user)

        self.formLayout.itemAt(self.formLayout.count()-2).widget().setStyleSheet(
            "background-color:transparent;border: 0px solid white;border-radius:20px;color:white;")
        self.formLayout.itemAt(self.formLayout.count(
        )-2).widget().setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.formLayout.itemAt(self.formLayout.count(
        )-1).widget().clicked.connect(self.clickedBtn_user)

        self.formLayout.itemAt(self.formLayout.count()-1).widget().setStyleSheet(
            "background-color: white;border: 1px solid lightgray;border-radius: 17px;font-size: 20px;")
        self.formLayout.itemAt(self.formLayout.count(
        )-1).widget().setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.messege_time = QLabel(datetime.datetime.now().strftime(
            "%H:%M"), alignment=Qt.AlignRight)
        self.messege_time.setStyleSheet("color: black")
        self.messege_time.setStyleSheet(
            "background-color: transparent;border: 0px solid lightgray;border-radius: 5px;font-size: 14px;")
        self.id = QLabel('')
        # self.seen_image.setIcon(QIcon(os.path.abspath(os.getcwd()+'/icons/reply.png')))
        self.id.setStyleSheet(
            "background-color: transparent;border: 0px none;border-radius: 10px;font-size: 1px;")

        self.formLayout.addRow(self.id, self.messege_time)
        self.last_used = "other"

    def file_send(self):
        pass

    def emoji_v(self, from_f):
        self.messegebox_t.setText(
            self.messegebox_t.toPlainText()+emoji.emojize(from_f))

    def scrol_down(self):
        self.scrollArea.verticalScrollBar().setValue(
            self.scrollArea.verticalScrollBar().maximum())
        self.move_d_zout()

    def move_down_wheel(self):

        if self.scrollArea.verticalScrollBar().value() != self.scrollArea.verticalScrollBar().maximum():
            self.timer11 = QtCore.QTimer()
            self.timer11.timeout.connect(self.move_d_zin)
            self.timer11.start(4)
            self.send_b_11.setHidden(False)
        else:

            self.timer11 = QtCore.QTimer()
            self.timer11.timeout.connect(self.move_d_zout)
            self.timer11.start(4)
            # QTimer.singleShot(50, lambda:print(self.scrollArea.verticalScrollBar().value()))

    def move_d_zin(self):
        global zoom_smth2
        zoom_smth2 += 1

        self.send_b_11.resize(zoom_smth2, zoom_smth2)
        self.send_b_11.setIconSize(
            QSize(int(zoom_smth2/2+5), int(zoom_smth2/2+5)))
        self.send_b_11.setStyleSheet(
            "background-color: rgba(247, 247, 247, 1);border: 0px solid white;border-radius:%dpx;" % int(zoom_smth2/2))
        if zoom_smth2 >= 41:
            zoom_smth2 = 41
            self.timer11.stop()

    def move_d_zout(self):
        global zoom_smth2
        zoom_smth2 -= 1
        self.send_b_11.resize(zoom_smth2, zoom_smth2)
        self.send_b_11.setIconSize(
            QSize(int(zoom_smth2/2+5), int(zoom_smth2/2+5)))
        self.send_b_11.setStyleSheet(
            "background-color: rgba(247, 247, 247, 1);border: 0px solid white;border-radius:%dpx;" % int(zoom_smth2/2))
        if zoom_smth2 <= 0:
            zoom_smth2 = 0
            self.send_b_11.setHidden(True)
            self.timer11.stop()

    def move_down(self):
        global move_smth, zoom_smth
        self.setting_FRM.setGeometry(QtCore.QRect(move_smth, 0, 381, 581))
        move_smth -= 3
        zoom_smth -= 1
        self.profile_LBL.resize(zoom_smth, zoom_smth)
        self.profile_LBL.setStyleSheet(
            "border: 0px solid gray ;border-radius: %dpx;" % int(zoom_smth/2))
        if move_smth == -384:
            self.timer.stop()
            # move_smth=0

    def rec_sec(self):
        global rec_sec
        global rec_min
        rec_sec += 1

        if rec_sec == 60:
            rec_min += 1
            rec_sec = 0
        self.label_6.setText("%02d:%02d" % (rec_min, rec_sec))
        self.label_6.setStyleSheet(
            "background-color: transparent;border: 0px solid transparent;font-size: 20px;")

    def deleting_gif(self):
        movie = QtGui.QMovie(os.getcwd() + '/icons/rec_button.gif')
        self.record_b.setIcon(
            QIcon(QPixmap(os.path.abspath(os.getcwd() + '/icons/radio.png'))))
        self.label_7.setMovie(movie)
        movie.stop()
        self.emoji_BTN.setEnabled(True)
        self.messegebox_t.setEnabled(True)
        self.label_6.setHidden(True)
        self.label_7.setHidden(True)
        self.label_6.setEnabled(True)
        self.label_7.setEnabled(True)
        self.record_b.setEnabled(True)
        self.messegebox_t.setStyleSheet(
            "background-color:rgba(255, 255, 255,1);border: 1px solid lightgray;border-radius:15px;font-size: 18px;")
        self.timer4 = QtCore.QTimer()
        self.timer4.timeout.connect(self.resize_up_msgbox)
        self.timer4.start(2)

    def stop_rec(self):
        self.record_b.setChecked(True)
        self.record_b.setEnabled(False)
        self.label_6.setEnabled(False)
        self.label_7.setHidden(True)
        self.label_7.setEnabled(False)

        global rec_min
        global rec_sec
        self.exit_emoji_box()

        rec_min = 0
        rec_sec = 0
        self.timer.stop()

        self.label_8.setHidden(False)

        movie = QtGui.QMovie(
            os.getcwd() + '/icons/ezgif.com-gif-maker (5).gif')
        self.label_8.setMovie(movie)
        movie.start()
        QTimer.singleShot(2000, lambda: self.label_8.setHidden(True))
        QTimer.singleShot(2000, self.deleting_gif)
        # self.messegebox_t.resize(571, 31)

        self.send_b_13.setHidden(True)

    def start_rec_voice(self):
       
        filename = os.getcwd()+'/Files/'+'1.wav'
        # global record_until
        chunk = 1024
        FORMAT = pyaudio.paInt16
        channels = 1
        sample_rate = 44100
        p = pyaudio.PyAudio()
        # time of record
       
        stream = ''
        # try:
        stream = p.open(format=FORMAT, channels=channels, rate=sample_rate,input=True, output=True, frames_per_buffer=chunk)
        frames = []
        for i in range(int(44100 / chunk * 10)):
            data = stream.read(chunk)#save byte in moteghayer
            # data1 = [int(108), sender, recever,data]
            # stream.write(data)
            # frames.append(data)

        print("Finished recording.")
        stream.stop_stream()
        stream.close()
        p.terminate()
        # save audio file
        wf = wave.open(filename, "wb")
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(sample_rate)
        wf.writeframes(b"".join(frames))
        wf.close()
        return 0
           

            
        # except:

        #     global mic_port
        #     mic_port = False
        #     print('\033c')
        #     return 0
            
    def slider_over(self,itm,time):
        global play_sec
        play_sec+=1
        self.formLayout.itemAt(itm).widget().setValue(play_sec)
        
        if play_sec == time:
            play_sec = -1
            self.formLayout.itemAt(itm).widget().setValue(0)
            self.timer50.stop()

            
    def play_voice(self, voice_id,itm,play_t):
      
        thread = threading.Thread(target=lambda : playsound(os.getcwd()+'/Files/'+voice_id) )
        thread.start()
    
        self.timer50 = QtCore.QTimer()
        self.timer50.timeout.connect(lambda : self.slider_over(itm,play_t))
        self.timer50.start(1000)
        
        # print(mediainfo(os.getcwd()+'/Files/'+voice_id)['duration'])
        



    def rec_voice(self):
        global record_until
        self.exit_emoji_box()
        if self.record_b.isChecked():

            record_until = False
            self.voice_mess_me("1.wav")
            self.label_9.setHidden(False)
            movie = QtGui.QMovie(os.getcwd() + '/icons/sendmic.gif')
            self.label_9.setMovie(movie)
            movie.start()
            self.messegebox_t.setStyleSheet(
                "background-color:rgba(255, 255, 255,1);border: 1px solid lightgray;border-radius:15px;font-size: 18px;")
            global rec_min
            global rec_sec
            self.exit_emoji_box()
            self.label_6.setHidden(True)
            self.label_7.setHidden(True)

            rec_min = 0
            rec_sec = 0
            self.timer.stop()
            self.record_b.setIcon(
                QIcon(QPixmap(os.path.abspath(os.getcwd() + '/icons/radio.png'))))
            self.emoji_BTN.setEnabled(True)
            self.messegebox_t.setEnabled(True)

            # self.messegebox_t.resize(571, 31)

            self.timer14 = QtCore.QTimer()
            self.timer14.timeout.connect(lambda: self.label_9.setHidden(True))
            self.timer14.start(1000)

            self.timer4 = QtCore.QTimer()
            self.timer4.timeout.connect(self.resize_up_msgbox)
            self.timer4.start(2)

            self.send_b_13.setHidden(True)
            movie = QtGui.QMovie(os.getcwd() + '/icons/rec_button.gif')
            self.label_7.setMovie(movie)
            movie.stop()

        else:

            self.exit_emoji_box()
            self.messegebox_t.setStyleSheet(
                "background-color:rgba(248, 248, 248,.7);border: 1px solid lightgray;border-radius:15px;font-size: 18px;")
            # self.messegebox_t.setEnabled(False)
            self.label_6.setText("00:00")
            self.label_6.setStyleSheet(
                "background-color: transparent;border: 0px solid transparent;font-size: 20px;")

            record_until = True
            self.emoji_BTN.setEnabled(False)
            self.messegebox_t.setEnabled(False)
            # self.messegebox_t.resize(461, 31)
            self.timer4 = QtCore.QTimer()
            self.timer4.timeout.connect(self.resize_bk_msgbox)
            self.timer4.start(2)
            movie = QtGui.QMovie(os.getcwd() + '/icons/rec_button.gif')
            self.label_7.setMovie(movie)
            movie.start()

            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.rec_sec)
            self.timer.start(1000)
            self.timer22 = QtCore.QTimer()
            self.timer22.timeout.connect(self.cheack_port)
            self.timer22.start(1000)
            # threading.Thread(target=self.start_rec_voice, args=()).start()

            
    def cheack_port(self):
        global mic_port
      
        if mic_port==False:
            
            self.stop_rec()
            QMessageBox.about(self, "Mic Error", "The microphone is being used by another application")
            
            self.timer22.stop()

    def resize_bk_msgbox(self):
        global move_smth2
        self.messegebox_t.resize(move_smth2, 41)
        move_smth2 -= 1
        if move_smth2 == 401:
            self.record_b.setIcon(
                QIcon(QPixmap(os.path.abspath(os.getcwd() + '/icons/correct.png'))))
            self.label_6.setHidden(False)
            self.label_7.setHidden(False)
            self.send_b_13.setHidden(False)

            self.timer4.stop()

    def resize_up_msgbox(self):

        global move_smth2
        self.messegebox_t.resize(move_smth2, 41)
        move_smth2 += 1
        if move_smth2 == 571:
            self.timer4.stop()

    def contex_menu(self):
        menu = QMenu(self)
        info = newAct = menu.addAction("info")
        mute = menu.addAction("mute")
        clear_messages = menu.addAction("clear messages")
        Delete_Chat = menu.addAction("Delete Chat")
        info.triggered.connect(lambda: print("d0"))
        mute.triggered.connect(lambda: print("d1"))
        clear_messages.triggered.connect(self.clear_screen)
        Delete_Chat.triggered.connect(self.clear_screen)

        menu.exec_(QCursor.pos())

    def menu_back(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.move_down)
        self.timer.start(1)

    def move_ups(self):
        global move_smth, zoom_smth
        self.setting_FRM.setGeometry(QtCore.QRect(move_smth, 0, 381, 581))
        move_smth += 3
        zoom_smth += 1
        self.profile_LBL.resize(zoom_smth, zoom_smth)
        self.profile_LBL.setStyleSheet(
            "border: 0px solid gray ;border-radius: %dpx;" % int(zoom_smth/2))
        if move_smth == 3:
            self.timer.stop()

    def start_menu(self):

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.move_ups)
        self.timer.start(1)

    def move_ups_emoji_box(self):
        global move_smth1
        self.emoji_FRM.setGeometry(QtCore.QRect(390, move_smth1, 211, 91))
        move_smth1 -= 1

        resize = int(abs((move_smth1-401)/6-25))

        self.send_b_6.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_3.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_2.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_5.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_4.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_10.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_9.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_8.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_8.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_7.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_12.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_11.resize(zoom_smth2, zoom_smth2)
        self.emoji_FRM.setStyleSheet(
            "background-color: rgba(255, 255, 255, %.2f);border: 0px solid gray;font-size: 1px;border-radius:10px;" % (resize/25))
        if move_smth1 == 470:
            self.emoji_FRM.setHidden(False)
        if move_smth1 <= 401:

            self.timer2.stop()

    def start_emoji_box(self):

        self.emoji_BTN.setHidden(True)

        self.emoji_BTN_2.setHidden(False)

        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.move_ups_emoji_box)
        self.timer2.start(1)

    def move_down_emoji_box(self):
        global move_smth1
        self.emoji_FRM.setGeometry(QtCore.QRect(390, move_smth1, 211, 91))
        move_smth1 += 1
        resize = int(abs((move_smth1-401)/6-25))

        self.send_b_6.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_3.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_2.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_5.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_4.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_10.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_9.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_8.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_8.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_7.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))
        self.send_b_12.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);border: 0px solid gray;font-size: %dpx;border-radius:10px;" % (resize+1))

        self.emoji_FRM.setStyleSheet(
            "background-color: rgba(255, 255, 255, %.2f);border: 0px solid gray;font-size: 1px;border-radius:10px;" % (resize/25))
        if move_smth1 == 470:

            self.emoji_FRM.setHidden(True)

        if move_smth1 >= 472:

            self.timer2.stop()

    def exit_emoji_box(self):

        self.emoji_BTN.setHidden(False)

        self.emoji_BTN_2.setHidden(True)

        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.move_down_emoji_box)
        self.timer2.start(1)

    def click_camera_BTN(self):
        cv2.namedWindow("preview")
        vc = cv2.VideoCapture(0)

        if vc.isOpened():  # try to get the first frame
            rval, frame = vc.read()
        else:
            rval = False

        while rval:
            cv2.imshow("preview", frame)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27:  # exit on ESC
                break
        cv2.destroyWindow("preview")

    def click_attach(self):

        self.attach_b.setHidden(True)
        self.attach_b_2.setHidden(False)

        self.timer12 = QtCore.QTimer()
        self.timer12.timeout.connect(self.doc_moveup)
        self.timer12.start(5)
        self.camera_BTN.setHidden(False)
        self.doc_BTN.setHidden(False)

    def click_attach_2(self):
        self.attach_b.setHidden(False)
        self.attach_b_2.setHidden(True)
        self.timer12 = QtCore.QTimer()
        self.timer12.timeout.connect(self.doc_movedown)
        self.timer12.start(5)

    def doc_moveup(self):
        global zoom_smth3
        zoom_smth3 += 1

        self.doc_BTN.setIconSize(QSize(zoom_smth3, zoom_smth3))
        self.camera_BTN.setIconSize(QSize(zoom_smth3, zoom_smth3))
        self.doc_BTN.resize(zoom_smth3, zoom_smth3)
        self.doc_BTN.setStyleSheet(
            "background-color: transparent;border: 0px solid white;border-radius:%dpx;" % int(zoom_smth3/2))
        self.camera_BTN.resize(zoom_smth3, zoom_smth3)

        self.camera_BTN.setStyleSheet(
            "background-color: transparent;border: 0px solid white;border-radius:%dpx;" % int(zoom_smth3/2))

        if zoom_smth3 >= 51:
            zoom_smth3 = 51
            self.timer12.stop()

    def doc_movedown(self):
        global zoom_smth3
        zoom_smth3 -= 1
        self.doc_BTN.setIconSize(QSize(zoom_smth3, zoom_smth3))
        self.camera_BTN.setIconSize(QSize(zoom_smth3, zoom_smth3))
        self.doc_BTN.resize(zoom_smth3, zoom_smth3)
        self.doc_BTN.setStyleSheet(
            "background-color: transparent;border: 0px solid white;border-radius:%dpx;" % int(zoom_smth3/2))
        self.camera_BTN.resize(zoom_smth3, zoom_smth3)
        self.camera_BTN.setStyleSheet(
            "background-color: rtransparent;border: 0px solid white;border-radius:%dpx;" % int(zoom_smth3/2))

        if zoom_smth3 <= 0:
            zoom_smth3 = 0
            self.camera_BTN.setHidden(True)
            self.doc_BTN.setHidden(True)
            self.timer12.stop()

    def click_search(self):
        self.attach_b.setEnabled(False)
        self.messegebox_t.setEnabled(False)
        self.emoji_BTN.setEnabled(False)
        self.record_b.setEnabled(False)
        self.pv_LBL.setHidden(True)
        self.searchuser_b.setHidden(True)

        self.click_attach_2()
        # self.label.setHidden(False)
        # self.label.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')

        self.button_call.setHidden(True)
        self.menu_user_b.setHidden(True)
        self.usernamem_l.setHidden(True)
        self.lastseen_l.setHidden(True)

        # self.searchuser_b.setGeometry(QtCore.QRect(1010, 10, 31, 31))
        self.pushButton_2.setHidden(False)
        self.pushButton_2.setIcon(
            QIcon(os.path.abspath(os.getcwd() + '/icons/search.png')))

        self.pushButton.setHidden(False)
        self.pushButton.setIcon(
            QIcon(os.path.abspath(os.getcwd() + '/icons/back.png')))

        self.lineEdit.setHidden(False)
        self.lineEdit.setFocus()
        self.lineEdit.setStyleSheet(
            "background-color: white;border: 1px solid lightgray;border-radius:15px;")

    def back_from_search(self):
        self.attach_b.setEnabled(True)
        self.messegebox_t.setEnabled(True)
        self.record_b.setEnabled(True)
        self.emoji_BTN.setEnabled(True)
        self.pv_LBL.setHidden(False)
        self.searchuser_b.setHidden(False)

        # self.label.setHidden(True)

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
        fileName, _ = QFileDialog.getOpenFileName(
            self, "FileDialog", "", "All Files ();;Python Files (.py)", options=options)
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
        if self.scrollArea.verticalScrollBar().value() == self.scrollArea.verticalScrollBar().maximum():
            QTimer.singleShot(50, self.scrol_down)
        if self.textedit_messegebox.toPlainText().strip():
            massege_text = "\n   "
            self.user_image = QPushButton()
            self.user_image.setIcon(
                QIcon(os.path.abspath(os.getcwd()+'/icons/me.png')))
            self.user_image.setIconSize(QSize(35, 35))

            if len(self.textedit_messegebox.toPlainText()) <= 66:
                self.messege_user = QLabel(
                    "  " + self.textedit_messegebox.toPlainText(), self)
            else:
                i = 0
                while(len(massege_text)-8 <= len(self.textedit_messegebox.toPlainText())):

                    massege_text = massege_text + \
                        self.textedit_messegebox.toPlainText()[i:i+66]+"\n   "
                    i = 66+i
                self.messege_user = QLabel(massege_text, self)

            self.messege_user.setStyleSheet(
                "background-color: #D7FAB3;border: 0px solid lightgray;border-radius: 17px;font-size: 20px;")
            if self.last_used == "other":
                self.formLayout.addRow(QLabel())

            self.textedit_messegebox.clear()
            self.formLayout.addRow(self.user_image, self.messege_user)

            self.formLayout.itemAt(self.formLayout.count(
            )-2).widget().clicked.connect(self.clickedBtn_user)
            self.formLayout.itemAt(self.formLayout.count()-2).widget().setStyleSheet(
                "background-color:transparent;border: 0px solid white;border-radius:20px;color:white;")
            self.formLayout.itemAt(self.formLayout.count(
            )-2).widget().setCursor(QCursor(QtCore.Qt.PointingHandCursor))

            self.messege_time = QLabel(" 12:54 ", alignment=Qt.AlignRight)
            self.messege_time.setStyleSheet("color: black")
            self.messege_time.setStyleSheet(
                "background-color: white;border: 0px solid lightgray;border-radius: 5px;font-size: 14px;")
            self.seen_image = QLabel()
            self.seen_image.setPixmap(QPixmap(os.path.abspath(
                os.getcwd()+'/icons/not_seen.png')).scaledToWidth(20))
            self.formLayout.addRow(self.messege_time, self.seen_image)
            self.last_used = "me"

    def clickedBtn_other(self):

        if self.scrollArea.verticalScrollBar().value() == self.scrollArea.verticalScrollBar().maximum():
            QTimer.singleShot(50, self.scrol_down)
        self.user_image = QPushButton()
        self.user_image.setIcon(
            QIcon(os.path.abspath(os.getcwd()+'/icons/user.png')))
        self.user_image.setIconSize(QSize(35, 35))
        # self.user_image.setPixmap(QPixmap(os.path.abspath(os.getcwd()+'/icons/user.png')).scaledToWidth(35))
        self.messege_user = QLabel(" slm mmd")
        self.messege_user.setStyleSheet(
            "background-color: white;border: 1px solid lightgray;border-radius: 17px;font-size: 20px;")
        if self.last_used == "me":
            self.formLayout.addRow(QLabel())
        self.formLayout.addRow(self.user_image, self.messege_user)
        self.formLayout.itemAt(self.formLayout.count(
        )-2).widget().clicked.connect(self.clickedBtn_user)

        self.formLayout.itemAt(self.formLayout.count()-2).widget().setStyleSheet(
            "background-color:transparent;border: 0px solid white;border-radius:20px;color:white;")
        self.formLayout.itemAt(self.formLayout.count(
        )-2).widget().setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.messege_time = QLabel(datetime.datetime.now().strftime(
            "%H:%M"), alignment=Qt.AlignRight)
        self.messege_time.setStyleSheet("color: black")
        self.messege_time.setStyleSheet(
            "background-color: transparent;border: 0px solid lightgray;border-radius: 5px;font-size: 14px;")
        self.seen_image = QPushButton()
        # self.seen_image.setIcon(QIcon(os.path.abspath(os.getcwd()+'/icons/reply.png')))
        self.seen_image.setStyleSheet(
            "background-color: transparent;border: 0px solid white;border-radius: 10px;")
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight)
        self.formLayout.addRow(self.seen_image, self.messege_time)
        self.last_used = "other"

    def voice_mess_other(self):
        self.formLayout.addRow(QLabel())
        if self.scrollArea.verticalScrollBar().value() == self.scrollArea.verticalScrollBar().maximum():
            QTimer.singleShot(50, self.scrol_down)
        self.user_image = QPushButton()
        self.user_image.setIcon(
            QIcon(os.path.abspath(os.getcwd()+'/icons/user.png')))
        self.user_image.setIconSize(QSize(35, 35))
        if self.last_used == "me":
            self.formLayout.addRow(QLabel())
        self.seen_image = QPushButton()
        self.seen_image.setIcon(
            QIcon(os.path.abspath(os.getcwd()+'/icons/google-play.png')))
        self.seen_image.setStyleSheet(
            "background-color: white;border: 3px solid white;border-radius: 10px;")

        self.formLayout.addRow(self.user_image, self.seen_image)
        self.formLayout.itemAt(self.formLayout.count(
        )-2).widget().clicked.connect(self.clickedBtn_user)
        self.formLayout.itemAt(self.formLayout.count()-2).widget().setStyleSheet(
            "background-color:transparent;border: 0px solid white;border-radius:20px;color:white;")

        self.formLayout.itemAt(self.formLayout.count(
        )-2).widget().setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.formLayout.itemAt(self.formLayout.count(
        )-1).widget().clicked.connect(self.clickedBtn_user)

        self.formLayout.itemAt(self.formLayout.count(
        )-1).widget().setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.messege_time = QLabel(datetime.datetime.now().strftime(
            "%H:%M"), alignment=Qt.AlignRight)
        self.messege_time.setStyleSheet("color: black")
        self.messege_time.setStyleSheet(
            "background-color: transparent;border: 0px solid lightgray;border-radius: 5px;font-size: 14px;")

        self.voice = QSlider(Qt.Horizontal)

        self.voice.setMinimum(10)
        self.voice.setMaximum(30)
        ##
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight)
        self.formLayout.addRow(self.messege_time, self.voice)
        self.formLayout.itemAt(self.formLayout.count(
        )-1).widget().sliderReleased.connect(self.clickedBtn_user)

        self.formLayout.addRow(QLabel())
        self.formLayout.addRow(QLabel())
        self.last_used = "other"

    def voice_mess_me(self,connect_to):
        self.formLayout.addRow(QLabel())
        if self.scrollArea.verticalScrollBar().value() == self.scrollArea.verticalScrollBar().maximum():
            QTimer.singleShot(50, self.scrol_down)
        self.user_image = QPushButton()
        self.user_image.setIcon(
            QIcon(os.path.abspath(os.getcwd()+'/icons/me.png')))
        self.user_image.setIconSize(QSize(35, 35))
        if self.last_used == "other":
            self.formLayout.addRow(QLabel())
        self.seen_image = QPushButton()
        self.seen_image.setIcon(
            QIcon(os.path.abspath(os.getcwd()+'/icons/google-play.png')))
        self.seen_image.setStyleSheet(
            "background-color: #D7FAB3;border: 3px solid #D7FAB3;border-radius: 10px;")

        self.formLayout.addRow(self.user_image, self.seen_image)
        self.formLayout.itemAt(self.formLayout.count(
        )-2).widget().clicked.connect(self.clickedBtn_user)
        self.formLayout.itemAt(self.formLayout.count()-2).widget().setStyleSheet(
            "background-color:transparent;border: 0px solid white;border-radius:20px;color:white;")

        self.formLayout.itemAt(self.formLayout.count(
        )-2).widget().setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        
        self.formLayout.itemAt(self.formLayout.count()-1).widget().setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.messege_time = QLabel(datetime.datetime.now().strftime(
            "%H:%M"), alignment=Qt.AlignRight)
        self.messege_time.setStyleSheet("color: black")
        self.messege_time.setStyleSheet(
            "background-color: transparent;border: 0px solid lightgray;border-radius: 5px;font-size: 14px;")

        self.voice = QSlider(Qt.Horizontal)

        self.voice.setMinimum(0)
        self.voice.setMaximum(int(abs(float(mediainfo(os.getcwd()+'/Files/'+connect_to)['duration']))))
        ##
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight)
        self.formLayout.addRow(self.messege_time, self.voice)

        self.formLayout.itemAt(self.formLayout.count()-3).widget().clicked.connect(lambda : self.play_voice(connect_to,self.formLayout.count()-3,int(abs(float(mediainfo(os.getcwd()+'/Files/'+connect_to)['duration'])))) )


        self.formLayout.itemAt(self.formLayout.count(
        )-1).widget().sliderReleased.connect(self.clickedBtn_user)

        self.formLayout.addRow(QLabel())
        self.formLayout.addRow(QLabel())
        self.last_used = "me"

    def clickedBtn_user(self):
    
        itm = QListWidgetItem("\n Mohammad Hossein Fadavi\n")
        itm.setIcon(QIcon(os.path.abspath(os.getcwd()+'/icons/user.png')))
        self.listWidget.insertItem(0,itm)
        itm = QListWidgetItem("\n Mohammad h\n")
        itm.setIcon(QIcon(os.path.abspath(os.getcwd()+'/icons/user.png')))
        self.listWidget.insertItem(1,itm)
        itm = QListWidgetItem("\n Mohammad Hossein\n")
        itm.setIcon(QIcon(os.path.abspath(os.getcwd()+'/icons/user.png')))
        self.listWidget.insertItem(2,itm)
        
        self.listWidget.item(0).setWhatsThis('0')
        self.listWidget.item(1).setWhatsThis('1')
        self.listWidget.item(2).setWhatsThis('2')

        # self.listWidget.item(1).setForeground(QtCore.Qt.blue)
        # self.listWidget.item(1).setIcon(QIcon(os.path.abspath(os.getcwd()+'/icons/me.png')))
        # # self.listWidget.item(1).setText(self.listWidget.item(1).text()[0:-1]+"  +1\n")

    def textChanged_messege_event(self):

        if self.textedit_messegebox.toPlainText().strip():
            self.button_record.setHidden(True)
            self.button_send.setHidden(False)
        else:
            self.button_record.setHidden(False)
            self.button_send.setHidden(True)

    def clear_screen(self):
        for i in reversed(range(self.formLayout.count())):
            self.formLayout.itemAt(i).widget().deleteLater()


App = QApplication(sys.argv)
window2 = Window()
sys.exit(App.exec())
