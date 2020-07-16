import socket
import subprocess
import json
from queue import Queue
import threading
from PyQt5 import QtCore, QtGui, QtWidgets  # works for pyqt5
import time
from select import select
from PyQt5.QtWidgets import *  # UI
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from captcha.image import ImageCaptcha
from PyQt5 import uic
import sys
import os
from os import path
import random
import http.client as httplib
from playsound import playsound
from PyQt5 import QtCore
import re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import Qt
import hashlib, uuid
from PyQt5.QtCore import QTimer
import pyqrcode 
import png 
from pyqrcode import QRCode 
from requests import get, post
import json
import webbrowser
import jwt
import base64

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

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
from tkinter import filedialog
from tkinter import *
import os.path
from kavenegar import *
import face_recognition
import cv2
import numpy as np


q = Queue()
s = socket.socket()

# Server information
## 51.195.19.3
s.connect(('0.0.0.0', 1425))

email_changer = ''
data_user = []
code_g = 0

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
download_status= False
new_messeg = []
new_file = []

f=''
token='yasin78'
reciver='mhfa1380'
token='mhfa1380'
reciver='yasin78'

class user:
    def __init__(self):
        pass

    # ersal etelaat karbar jadid be samte server
    def login(self, s: socket, capcha_code):
        global window
        self.data = [int(100)]
        self.username = window.lineEdit_user.text()
        self.name = window.lineEdit_name.text()
        self.email = window.lineEdit_email.text()
        # cheak email is valid

        if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', self.email)):

            self.password = window.lineEdit_pass.text()
            self.capcha_label = window.lineEdit_capcha.text()
            to_chek_password = window.lineEdit_repass.text()
            if self.cheking_password(self.password, to_chek_password):
                self.data.append(self.username)
                self.data.append(self.name)
                self.data.append(self.email)
                hashedpass = hashlib.md5(self.password.encode()).hexdigest()
                hashedpass = hashedpass[0:-5] + hashedpass[5:-8]
                self.data.append(hashedpass)
                if self.capcha_label == str(capcha_code):
                    sending_to_server(s, self.data)
                    wating_form(True, "forget_e")
                else:
                    QMessageBox.about(window, "recapcha error", "capcha code is not true")
                    window.lineEdit.setFocus()
            else:
                window.lineEdit.clear()
                QMessageBox.about(window, "password error",
                                  "oh! try agian to enter password because they are not equal!")
                window.Username_LE_7.clear()
                window.Username_LE_7.setFocus()
        else:
            QMessageBox.about(window, "Invalid Email", "enter valid email")
            window.Usename_LE_3.clear()
            window.Usename_LE_3.setFocus()
            window.lineEdit.clear()

    # tabe baraye chek kardan motabegh budan password
    def cheking_password(self, pass1, pass2):
        if pass1 == pass2:
            return True
        else:
            return False

    def get_code_server_rigister(self, s: socket, data: list):
        global code_g
        global data_user
        global window
        window.Username_LE_16.clear()
        window.Username_LE_16.setFocus()
        time.sleep(2)
        wating_form(False, "")
        window.go_to_emailverify_signup()
        data_user = data
        code_g = data[-1]
        print(code_g)

    def email_verify(self):
        global code_g
        global window
        global data_user
        print(code_g)
        # self.code_enter_box()
        if window.lineEdit_code_signup.text() == str(code_g):
            wating_form(True, "signup_f")
            self.data1 = [int(102)] + data_user
            sending_to_server(s, self.data1)
        else:
            window.Username_LE_16.clear()
            window.Username_LE_16.setFocus()
            QMessageBox.about(window, "Invalid Code", "Code is not correct")

    #     # pasokh server be inke aya ba movafaghiat user jadid ra
    #     # be data base ezafe karde ya kheir
    def server_added_user_to_database(self, s: socket, data: list):
        # self.meesege_box(data[0])
        global window
        # QMessageBox.about(window, "My box", "hi")
        if data[0] == "welcome to pychat !":
            time.sleep(7)
            wating_form(False, "")
            window.Signup_FRM.setGeometry(QtCore.QRect(22000, 0, 801, 541))
            window.Signin_FRM.setGeometry(QtCore.QRect(0, 0, 801, 541))
            window.Recover_FRM_4.setGeometry(QtCore.QRect(22000, 0, 801, 541))
            window.Username_LE.clear()
            window.Password_LE.clear()
            window.Username_LE.setFocus()
        elif data[0] == 'Error While Sending Email !':
            wating_form(False,'')
            wating_form(True,'no_response')
            
        time.sleep(1)
        wating_form(False, "")
        notification(data[0])

    def user_want_sign_in(self, s: socket):
        global window
        self.data = [int(103)]
        self.username = window.lineEdit_username.text()
        self.data.append(self.username)
        self.password = window.lineEdit_password.text()
        hashedpass = hashlib.md5(self.password.encode()).hexdigest()
        hashedpass = hashedpass[0:-5] + hashedpass[5:-8]
        self.data.append(hashedpass)
        sending_to_server(s, self.data)

    def forgot_password(self, s: socket):
        global window
        global email_changer
        self.eemail = window.lineEdit_forgetemail.text()
        if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', self.eemail)):
            email_changer = self.eemail
            data = [int(101), 'forgot', '_', self.eemail]
            sending_to_server(s, data)
            wating_form(True, "forget_e")
        else:
            QMessageBox.about(window, "Invalid Email", "enter valid email")
            window.Username_LE_2.clear()
            window.Username_LE_2.setFocus()

    def get_code_server(self, s: socket, data: list):
        global code_g
        global window
        code_g = data[-1]
        print(code_g)
        window.Recover_FRM.setGeometry(QtCore.QRect(-3000, 0, 801, 541))
        window.Recover_FRM_2.setGeometry(QtCore.QRect(0, 0, 801, 541))
        window.Username_LE_4.setText(window.Username_LE_2.text())
        wating_form(False, "")
        window.Username_LE_3.clear()
        window.Username_LE_3.setFocus()

    def change_pass(self):
        global window
        global email_changer

        pas = window.lineEdit_forget_pass.text()
        pas2 = window.lineEdit_forget_repass.text()
        if self.cheking_password(pas, pas2) and pas != '':
            hashedpass = hashlib.md5(pas.encode()).hexdigest()
            hashedpass = hashedpass[0:-5] + hashedpass[5:-8]
            data1 = [int(107), email_changer, hashedpass]
            sending_to_server(s, data1)
            wating_form(True, "signup_e")
        else:
            window.Username_LE_5.clear()
            window.Username_LE_5.setFocus()
            window.Username_LE_6.clear()
            QMessageBox.about(window, "Invalid Pass", "password doesnt match!")

    def check_mail_forgotpass(self):
        global code_g
        global window
        print("email cheak")
        print(code_g)
        if str(code_g) == str(window.lineEdit_forgetcode.text()):
            window.Username_LE_5.clear()
            window.Username_LE_5.setFocus()
            window.Username_LE_6.clear()
            window.Recover_FRM_2.setGeometry(QtCore.QRect(-2000, 0, 801, 541))
            window.Recover_FRM_3.setGeometry(QtCore.QRect(0, 0, 801, 541))
        else:
            window.Username_LE_3.clear()
            window.Username_LE_3.setFocus()
            QMessageBox.about(window, "Invalid Code", "Code is not correct")

    def password_changed(self, s: socket, data: list):
        global window
        time.sleep(3)
        wating_form(False, "")
        window.Recover_FRM_3.setGeometry(QtCore.QRect(4555000, 4000, 801, 541))
        window.Signin_FRM.setGeometry(QtCore.QRect(0, 0, 801, 541))
        window.Username_LE.clear()
        window.Password_LE.clear()
        window.Username_LE.setFocus()
        notification(str(data[0]))

    def send_text_message(self,s:socket,sender,reciver,message):
        
        message_time=str(datetime.datetime.now())
        message_id=str(time.time())
        message_id=str(sender)+str(reciver)+message_id[:-3]
        data=[int(106),sender,reciver,message,message_time,message_id,'t']
        sending_to_server(s,data)

    def send_file(self, s: socket,sender,reciver,usage,file_patch):
        
        # root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=( ("all files", "*.*"),("jpeg files", "*.jpg"),("ppng files", "*.png")))
        name, ext = os.path.splitext(file_patch)
        x = os.path.getsize(file_patch) #size
        send_time=str(datetime.datetime.now())[:-4]
        media_id=str(sender)+str(reciver)+send_time
        media_id=media_id.replace(":","-")
        media_id=media_id.replace(' ','-')
        media_id=media_id.replace('.','-')
    
        down=0
        data = [int(108), sender,reciver,str(x),ext,b'start'.hex(),media_id,usage]  # pasvand file + size file
        sending_to_server(s, data)
        f = open(file_patch, 'rb')
        while True:
            l = f.read(20480)

            while (l):
                # f"{str(x)}{ext}{l}".encode()
                down = down + 20480
                percent = (100 * float(down) / float(x))-0.03
                print("{:.2f} %".format(percent),end="--")
                data = [int(108), sender,reciver,str(x),ext,l.hex(),media_id,usage,send_time]  # pasvand file + size file
                sending_to_server(s, data)
                l = f.read(20480)
            if not l:
                data = [int(108), sender,reciver,str(x),ext,b'end'.hex(),media_id,usage,send_time]
                sending_to_server(s, data)
                print("sended")
                break


def recive_message(s:socket,data:list):
    global reciver,new_messeg
    # notification(f'{len(data)} new message!')
   
    for mes in data:
        if mes[-1]=="t":
            
            if reciver == mes[0] and token != mes[0]:
                new_mes2 = []
                new_mes2.append('t')
                new_mes2.append(mes[2])
                new_mes2.append(mes[3])
                new_messeg = new_mes2
                
                
                pass
                
                
        elif mes[-1]=='v':
            print(f"voice message from {mes[0]} ---> address in our server is {mes[2]}")
            key=input("do you want to download this file?  enter Y or N ")
            if key=='Y':
                sending_to_server(s,[int(120),mes[2]])
            else:
                continue

        elif mes[-1]=='m':
            if reciver == mes[0] and token != mes[0]:
                new_mes2 = []
                new_mes2.append('m')
                new_mes2.append(mes[2])
                new_messeg = new_mes2

                
            # if key=='Y':
            #     pass
            # else:
            #     continue

def receve_file(s:socket,data:list):
    global f,download_status
    recived_f = data[1]
    if bytes.fromhex(data[0])==b"start":
        f = open(recived_f, "wb")
    elif bytes.fromhex(data[0])==b"end":
        print(f"file from {data[0]} recived")
        f.close()
        download_status = True
    else:
        f.write(bytes.fromhex(data[0]))
    
# ----------------------------------------------------------------------------------------------other func ------------------
def wating_form(wating_until, form):
    global window
    if (wating_until):
        if cheak_net() == False:
            window.pushButton_7.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/error.png')))
            window.label_18.setHidden(False)
            window.label_18.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')
            movie = QtGui.QMovie(os.getcwd() + '/UI/Login/images/conection2.gif')
            window.label_18.setMovie(movie)
            movie.start()
            threading.Thread(target=window.net_conncted, args=()).start()
        elif form == 'no_response':
            window.pushButton_7.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/error.png')))
            window.label_18.setHidden(False)
            window.label_18.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')
            movie = QtGui.QMovie(os.getcwd() + '/UI/Login/images/conection2.gif')
            window.label_18.setMovie(movie)
            movie.start()

        elif form == 'signin':
            window.pushButton_7.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/error.png')))
            window.label_18.setHidden(False)
            window.label_18.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')
            movie = QtGui.QMovie(os.getcwd() + '/UI/Login/images/loading2.gif')
            window.label_18.setMovie(movie)
            movie.start()
        elif form == 'signup_e':
            # window.pushButton_7.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/error.png')))
            window.label_18.setHidden(False)
            window.label_18.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')
            movie = QtGui.QMovie(os.getcwd() + '/UI/Login/images/loading3.gif')
            window.label_18.setMovie(movie)
            movie.start()
        elif form == 'signup_f':
            window.pushButton_7.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/error.png')))
            window.label_18.setHidden(False)
            window.label_18.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')
            movie = QtGui.QMovie(os.getcwd() + '/UI/Login/images/loading.gif')
            window.label_18.setMovie(movie)
            movie.start()
        elif form == 'forget_e':
            window.pushButton_7.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/error.png')))
            window.label_18.setHidden(False)
            window.label_18.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')
            movie = QtGui.QMovie(os.getcwd() + '/UI/Login/images/loading4.gif')
            window.label_18.setMovie(movie)
            movie.start()
    else:
        time.sleep(1)
        window.pushButton_7.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/cross.png')))
        window.label_18.setHidden(True)


# ----------------network connections with Queue--------------------------------

# in tabe tamame dade haye vorude be barname ra misanjad agar daraye etebar bashad
# an hara accsept  mikonad
def _accsepting(s: socket):
    data = b''
    while True:
        time.sleep(0.02)
        try:
            # do taye dg niaz nabod
            r, _, _ = select([s], [s], [])  # baresi mishe vasl hast ya na
            if r:
                d = s.recv(4096)
                data += d
                if len(d) < 4096:
                    if data:
                        d = data.split(b'\0')
                        # extera baraye dycrypt ezafe beshe
                        # load_data(decrypt(d[i]))
                        for i in range(len(d) - 1):
                            load_data(d[i])
                            data = d[-1]
                    else:
                        s.close()
        except Exception as inst:
            print(inst)
            return


# in tabe vorudi haue ghbel pardazesh ke az tabee marhale
# ghabl amade ra decode mikonad va zemnan az halat json kharej
# mikonad va an ha ra darun q put mikonad
def load_data(data):
    x = (json.loads(data.decode()))
    q.put(x)


# ba farakhani in tabe har data ghbel fahm baraye server ra ersal
# mikonim  in tabee khodkar tamame vorudi ash ra be json tablil karde
# va baad an ra ra encode mikond va ersal be server
# vorudi in tabe sheye s hast ke bala az ruye socket sakhtim
def sending_to_server(socket: socket, data):
    data = json.dumps(data)
    socket.send((data.encode() + b'\0'))


# in tabe kar ha va darkhast hayie ke az samte server amade ra inja ejra mikonad
def do_work(obj: user, s: socket):
    while True:
        time.sleep(0.03)
        if not q.empty():
            new_data = q.get()
            task = new_data[0]
            obj_work[f"{task}"](s, new_data[1:])
            q.task_done()


obj = user()
obj_work={ 'token':"yasin78",
      '500':obj.email_verify,
      '502':obj.server_added_user_to_database,
      '509':obj.check_mail_forgotpass,
      '504':obj.password_changed,
      '503':recive_message,
    #   '509':obj.profile_changed,
      '510':receve_file,

 
      }

threading.Thread(target=_accsepting, args=(s,)).start()
threading.Thread(target=do_work, args=(obj, s)).start()


# cheak network
def cheak_net():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False


# PopUP Notification namayesh midahad
def notification(messege):
    img = os.path.abspath(os.getcwd() + '/Other/icon.png')
    subprocess.Popen(["notify-send", "-i", img, "PyChat", messege])
    playsound('Other/notify.mp3')


# sakhte image recapcha
# _________________________________________________________________________________________________UI_______________


class UI_login(QMainWindow):
    def __init__(self):
        global obj
        self.capcha_code = 0
        super(UI_login, self).__init__()
        uic.loadUi("UI/Login/Login_F.ui", self)
        self.offset = None
        radius = 35.0
        path = QtGui.QPainterPath()
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        # self.button_forget = self.findChild(QPushButton, "forgotpass_b")
        self.lineEdit_username = self.findChild(QLineEdit, "Username_LE")
        self.lineEdit_password = self.findChild(QLineEdit, "Password_LE")
        self.lineEdit_name = self.findChild(QLineEdit, "Password_LE_3")
        self.lineEdit_code_signup = self.findChild(QLineEdit, "Username_LE_16")
        self.lineEdit_user = self.findChild(QLineEdit, "Usename_LE_4")
        self.lineEdit_email = self.findChild(QLineEdit, "Usename_LE_3")
        self.lineEdit_pass = self.findChild(QLineEdit, "Password_LE_4")
        self.lineEdit_repass = self.findChild(QLineEdit, "Username_LE_7")
        self.lineEdit_capcha = self.findChild(QLineEdit, "lineEdit")
        self.label_capcha = self.findChild(QLabel, "label")
        self.lineEdit_forgetemail = self.findChild(QLineEdit, "Username_LE_2")
        self.lineEdit_forgetcode = self.findChild(QLineEdit, "Username_LE_3")
        self.lineEdit_forget_pass = self.findChild(QLineEdit, "Username_LE_5")
        self.lineEdit_forget_repass = self.findChild(QLineEdit, "Username_LE_6")
        self.label_18.setHidden(True)
        self.capcha()
        # window.label_18.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')
        self.label_background = self.findChild(QLabel, "background")
        self.label_background.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/UI/Login/images/background.jpg')))
        self.label_background = self.findChild(QLabel, "label_3")
        self.label_background.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/UI/Login/images/background.jpg')))
        self.label_background = self.findChild(QLabel, "label_4")
        self.label_background.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/UI/Login/images/background.jpg')))
        self.label_background = self.findChild(QLabel, "label_5")
        self.label_background.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/UI/Login/images/background.jpg')))
        self.label_background = self.findChild(QLabel, "label_5")
        self.label_background.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/UI/Login/images/background.jpg')))
        self.label_background = self.findChild(QLabel, "label_6")
        self.label_background.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/UI/Login/images/background.jpg')))

        movie = QtGui.QMovie(os.getcwd() + '/UI/Login/images/sidebar.gif')
        self.label_2.setMovie(movie)
        self.label_9.setMovie(movie)
        self.label_21.setMovie(movie)
        self.label_22.setMovie(movie)
        self.label_25.setMovie(movie)
        self.label_26.setMovie(movie)
        # self.label_2.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/UI/Login/images/sidebar.png')))
        # self.label_9.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/UI/Login/images/sidebar.png')))
        # self.label_21.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/UI/Login/images/sidebar.png')))
        # self.label_22.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/UI/Login/images/sidebar.png')))
        # self.label_25.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/UI/Login/images/sidebar.png')))
        # self.label_26.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/UI/Login/images/sidebar.png')))

        movie.start()
        self.Username_LE.setFocus()
        self.Signup1_BTN.clicked.connect(self.Go_to_signup)
        self.pushButton.clicked.connect(self.Back_from_signup_to_signin)
        self.Forgotpass_BTN_2.clicked.connect(self.Go_to_recovery)
        self.Signin_BTN_2.clicked.connect(self.Go_to_varify)
        self.pushButton_6.clicked.connect(self.Back_from_recoverpass_to_signin)
        self.pushButton_4.clicked.connect(self.Back_from_varify_to_recoverpass)
        self.pushButton_5.clicked.connect(self.Back_from_changepass_to_varify)
        self.pushButton_13.clicked.connect(self.Go_to_signup)
        self.Forgotpass_BTN_3.setStyleSheet("background-color: transparent;color:white;")
        self.Forgotpass_BTN_4.setStyleSheet("background-color: transparent;color:white;")
        self.Forgotpass_BTN_3.clicked.connect(self.cheak_qrcode_forget)
        self.Forgotpass_BTN_4.clicked.connect(self.cheak_qrcode_signup)

        self.pushButton_3.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/yahoo.png')))
        self.pushButton_3.setStyleSheet(
            "background-color:transparent;border: 0px solid white;border-radius:20px;color:white;")
        self.pushButton_3.clicked.connect(self.yahoo_signup)

        self.Signin_BTN_5.clicked.connect(obj.change_pass)
        self.pushButton_5.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/back.png')))
        self.pushButton_4.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/back.png')))
        self.pushButton_13.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/iages/back.png')))
        self.pushButton_6.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/back.png')))
        self.pushButton_5.setStyleSheet("background-color:transparent;border: 0px solid black;border-radius:10px;")
        self.pushButton_4.setStyleSheet("background-color:transparent;border: 0px solid black;border-radius:10px;")
        self.pushButton_13.setStyleSheet("background-color:transparent;border: 0px solid black;border-radius:10px;")
        self.pushButton_6.setStyleSheet("background-color:transparent;border: 0px solid black;border-radius:10px;")
        self.frame_20.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')

        self.Signin_BTN.clicked.connect(self.clickedBtn_login)
        self.pushButton_8.clicked.connect(self.yahoo_signin)
        self.pushButton_8.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/yahoo.png')))
        self.pushButton_8.setStyleSheet(
            "background-color:transparent;border: 0px solid white;border-radius:20px;color:white;")
        self.Signin_BTN.setStyleSheet(
            "background-color:  rgb(58, 175, 159);border: 1px solid rgb(58, 175, 159);border-radius:20px;color:white;")
        self.Signup1_BTN.setStyleSheet(
            "background-color: transparent;border: 1px solid white;border-radius:20px;color:white;")
        self.Signin_BTN_2.setStyleSheet(
            "background-color:  rgb(58, 175, 159);border: 1px solid rgb(58, 175, 159);border-radius:15px;color:white;")
        self.Signup1_BTN_7.setStyleSheet(
            "background-color: transparent;border: 1px solid white;border-radius:20px;color:white;")
        self.Username_LE_3.setStyleSheet(
            "background-color: transparent;border: 1px solid white;border-radius:20px;color:white;")
        self.Username_LE_16.setStyleSheet(
            "background-color: transparent;border: 1px solid white;border-radius:20px;color:white;")
        self.Signin_BTN_4.setStyleSheet(
            "background-color:  rgb(165, 165, 165);border: 1px solid rgb(58, 175, 159);border-radius:20px;color:white;")
        self.pushButton.setStyleSheet(
            "background-color: transparent;border: 1px solid white;border-radius:20px;color:white;")
        self.Signin_BTN_3.setStyleSheet(
            "background-color:  rgb(58, 175, 159);border: 1px solid rgb(58, 175, 159);border-radius:15px;color:white;")
        self.Signup1_BTN_2.setStyleSheet(
            "background-color: transparent;border: 1px solid white;border-radius:20px;color:white;")
        self.Signin_BTN_5.setStyleSheet(
            "background-color:  rgb(58, 175, 159);border: 1px solid rgb(58, 175, 159);border-radius:20px;color:white;")
        self.frame_6.setStyleSheet("background-color:  rgb(58, 175, 159);")
        self.Signin_BTN_3.clicked.connect(self.clickedBtn_rigister)
        self.pushButton_2.clicked.connect(self.capcha)
        # self.Forgotpass_BTN_2.clicked.connect(self.clickedBtn_forget)
        self.pushButton_7.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/cross.png')))
        self.pushButton_7.setStyleSheet("background-color: transparent;border: 0px solid white;")
        self.pushButton_7.clicked.connect(self.close_win)
        self.Signup1_BTN_2.clicked.connect(obj.check_mail_forgotpass)
        self.Signup1_BTN_7.clicked.connect(obj.email_verify)
        self.center()
        self.show()

    def yahoo_signup(self):
        self.pushButton_7.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/error.png')))
        self.label_18.setHidden(False)
        self.label_18.setStyleSheet('background-color:rgba(255, 255, 255, 0.2);')
        movie = QtGui.QMovie(os.getcwd() + '/UI/Login/images/conection.gif')
        self.label_18.setMovie(movie)
        movie.start()
        ############################
        client_id = 'dj0yJmk9YUc0Z1NNS1VMYzJCJmQ9WVdrOU1IcEZPVmt6TXpnbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTZj'
        client_secret = '99921476f30c4fa680ba5452549ccc9342253b2d'
        base_url = 'https://api.login.yahoo.com/'
        code_url = f'oauth2/request_auth?client_id={client_id}&redirect_uri=oob&response_type=code&language=en-us'
        webbrowser.open(base_url + code_url)
        encoded = base64.b64encode((client_id + ':' + client_secret).encode("utf-8"))
        headers = {
            'Authorization': f'Basic {encoded.decode("utf-8")}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        text, ok = QInputDialog.getText(self, 'Yahoo!', 'Enter Yahoo Code:')
        if ok:

            code = str(text)

            data = {
                'grant_type': 'authorization_code',
                'redirect_uri': 'oob',
                'code': code
            }
            response = post(base_url + 'oauth2/get_token', headers=headers, data=data)
            if (response.ok):
                headers = {
                    'Authorization': f'Bearer {response.json()["access_token"]}',
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                }

                response2 = get('https://api.login.yahoo.com/openid/v1/userinfo', headers=headers)
                if (response2.ok):
                    self.Password_LE_3.setText(response2.json()['name'])
                    self.Usename_LE_4.setText(response2.json()['nickname'])
                    self.Usename_LE_3.setText(response2.json()['email'])
                    image = response2.json()['picture']
                    self.Password_LE_4.setFocus()

                    ##############################
                    import urllib.request
                    urllib.request.urlretrieve(image, '%s.jpg' % response2.json()['nickname'])
                else:
                    QMessageBox.about(self, "signup error", "illegal access!")
            else:
                QMessageBox.about(self, "signup error", "The unexpected error happened!")
                self.Password_LE_3.setFocus()

            #####################

        window.pushButton_7.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/cross.png')))
        window.label_18.setHidden(True)

    def yahoo_signin(self):
        self.pushButton_7.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/error.png')))
        self.label_18.setHidden(False)
        self.label_18.setStyleSheet('background-color:rgba(255, 255, 255, 0.2);')
        movie = QtGui.QMovie(os.getcwd() + '/UI/Login/images/conection.gif')
        self.label_18.setMovie(movie)
        movie.start()
        ############################
        client_id = 'dj0yJmk9YUc0Z1NNS1VMYzJCJmQ9WVdrOU1IcEZPVmt6TXpnbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTZj'
        client_secret = '99921476f30c4fa680ba5452549ccc9342253b2d'
        base_url = 'https://api.login.yahoo.com/'
        code_url = f'oauth2/request_auth?client_id={client_id}&redirect_uri=oob&response_type=code&language=en-us'
        webbrowser.open(base_url + code_url)
        encoded = base64.b64encode((client_id + ':' + client_secret).encode("utf-8"))
        headers = {
            'Authorization': f'Basic {encoded.decode("utf-8")}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        text, ok = QInputDialog.getText(self, 'Yahoo!', 'Enter Yahoo Code:')

        if ok:

            code = str(text)

            data = {
                'grant_type': 'authorization_code',
                'redirect_uri': 'oob',
                'code': code
            }

            response = post(base_url + 'oauth2/get_token', headers=headers, data=data)
            if (response.ok):
                headers = {
                    'Authorization': f'Bearer {response.json()["access_token"]}',
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                }

                response2 = get('https://api.login.yahoo.com/openid/v1/userinfo', headers=headers)
                if (response2.ok):
                    self.Username_LE.setText(response2.json()['nickname'])
                    self.Password_LE.setText('3d6c1bd47f109e34c02f08773f8bd47f109e34c02f0877')
                    self.clickedBtn_login()
                    self.Username_LE.setText('')
                    self.Password_LE.setText('')
                else:
                    self.Username_LE.setText('')
                    self.Password_LE.setText('')
                    QMessageBox.about(self, "signin error", "illegal access!")

                    ##############################

            else:
                self.Username_LE.setText('')
                self.Password_LE.setText('')
                QMessageBox.about(self, "signin error", "The unexpected error happened!")

            #####################

        window.pushButton_7.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/cross.png')))
        window.label_18.setHidden(True)

    def cheak_qrcode_forget(self):

        global obj
        cap = cv2.VideoCapture(0)
        # font = cv2.FONT_HERSHEY_PLAIN
        clos_e = True
        while clos_e:
            _, frame = cap.read()
            decodedObjects = pyzbar.decode(frame)

            for data_code in decodedObjects:
                (x, y, w, h) = data_code.rect
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.rectangle(gray, (x + 2, y + 2), (x + 2 + w, y + 2 + h), (0, 0, 255), 4)
                cv2.imshow("Frame", gray)

                # time.sleep(3)
                playsound('Other/beep.mp3')
                self.Username_LE_3.setText(data_code.data.decode("utf-8"))
                time.sleep(1)
                obj.check_mail_forgotpass()
                clos_e = False
                # cv2.putText(frame, str(obj.data), (50, 50), font, 2,(255, 0, 0), 3)
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1)
            if key == 27:
                break
        cv2.destroyAllWindows()

    def cheak_qrcode_signup(self):

        global obj
        cap = cv2.VideoCapture(0)
        # font = cv2.FONT_HERSHEY_PLAIN
        clos_e = True
        while clos_e:
            _, frame = cap.read()
            decodedObjects = pyzbar.decode(frame)

            for data_code in decodedObjects:
                (x, y, w, h) = data_code.rect
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.rectangle(gray, (x + 2, y + 2), (x + 2 + w, y + 2 + h), (0, 0, 255), 4)
                cv2.imshow("Frame", gray)

                playsound('Other/beep.mp3')
                self.Username_LE_16.setText(data_code.data.decode("utf-8"))
                time.sleep(1)
                obj.email_verify()
                clos_e = False

            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1)
            if key == 27:
                break
        cv2.destroyAllWindows()

    def net_conncted(self):
        while (not cheak_net()):
            time.sleep(2)
        wating_form(False, "")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def close_win(self):
        self.close()

    def capcha(self):
        img = ImageCaptcha()
        rnd_num = random.randint(10000, 100000)
        image = img.generate_image(str(rnd_num))
        image.save("Other/random.jpeg")
        self.label_capcha.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/Other/random.jpeg')))
        self.capcha_code = rnd_num
        self.lineEdit.clear()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def go_to_emailverify_signup(self):
        self.Recover_FRM_4.setGeometry(QtCore.QRect(0, 0, 801, 541))

    def Go_to_signup(self):
        self.Signin_FRM.setGeometry(
            QtCore.QRect(22000, 0, 801, 541))  # dge nabayad to x=22000 ui bezaram chon mishe zir majmoaash
        self.Signup_FRM.setGeometry(QtCore.QRect(0, 0, 801, 541))
        self.Password_LE_3.clear()
        self.Usename_LE_4.clear()
        self.Usename_LE_3.clear()
        self.Password_LE_4.clear()
        self.Username_LE_7.clear()
        self.Recover_FRM_4.setGeometry(QtCore.QRect(22000, 0, 801, 541))
        self.lineEdit.clear()
        self.Password_LE_3.setFocus()

    def Back_from_signup_to_signin(self):
        self.Signup_FRM.setGeometry(QtCore.QRect(22000, 0, 801, 541))
        self.Signin_FRM.setGeometry(QtCore.QRect(0, 0, 801, 541))
        self.Username_LE.clear()
        self.Password_LE.clear()
        self.Username_LE.setFocus()

    def Go_to_recovery(self):
        self.Signin_FRM.setGeometry(QtCore.QRect(-1000, 0, 801, 541))
        self.Recover_FRM.setGeometry(QtCore.QRect(0, 0, 801, 541))
        self.Username_LE_2.clear()
        self.Username_LE_2.setFocus()

    def Go_to_varify(self):
        obj.forgot_password(s)

    def Back_from_recoverpass_to_signin(self):
        self.Recover_FRM.setGeometry(QtCore.QRect(25000, 0, 801, 541))
        self.Signin_FRM.setGeometry(QtCore.QRect(0, 0, 801, 541))
        self.Username_LE.clear()
        self.Password_LE.clear()
        self.Username_LE.setFocus()

    def Back_from_varify_to_recoverpass(self):
        self.Recover_FRM_2.setGeometry(QtCore.QRect(35000, 0, 801, 541))
        self.Recover_FRM.setGeometry(QtCore.QRect(0, 0, 801, 541))

    def Back_from_changepass_to_varify(self):
        self.Recover_FRM_3.setGeometry(QtCore.QRect(4555000, 4000, 801, 541))
        self.Recover_FRM_2.setGeometry(QtCore.QRect(0, 0, 801, 541))

    def clickedBtn_login(self):  # login page run mishe
        obj.user_want_sign_in(s)  # dokme login aval
        wating_form(True, "signin")

    def clickedBtn_rigister(self):  # OPEN RIGISTER PAGE
        obj.login(s, self.capcha_code)
        self.capcha()


class UI_Ads(QMainWindow):
    def __init__(self):
        super(UI_Ads, self).__init__()
        uic.loadUi("UI/Ads/Ads.ui", self)
        self.offset = None
        radius = 10.0
        path = QtGui.QPainterPath()
        img = QPixmap(os.path.abspath(os.getcwd() + '/UI/Ads/images/Ads.png'))
        self.ads_l.setPixmap(img)
        self.ads_l.setFixedWidth(img.width())
        self.ads_l.setFixedHeight(img.height())
        self.exit_b.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Ads/images/cross.png')))
        self.exit_b.setStyleSheet("background-color: transparent;border: 0px solid white;")
        self.exit_b.move(img.width() - 32, 10)
        self.exit_b.clicked.connect(self.close)
        self.setFixedSize(self.ads_l.size())
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.show()


class UI_Master(QMainWindow):
    last_used = ""

    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.abspath(os.getcwd() + "/UI/Master/Chat_box.ui"), self)
        global token,reciver,s,obj
        im_online=[int(105),token]
        sending_to_server(s,im_online)

        # with open("theme.txt") as file: # Use file to refer to the file object
        #     data = file.read()
        #     print (data)

        self.setFixedSize(1051, 560)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint |
                            QtCore.Qt.WindowMinimizeButtonHint)
        
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
        self.label_11.setStyleSheet("background-color: white;border: 0px solid gray;border-radius:10px;color:rgb(0, 0, 0);font-size: 14px;")
        self.label_12.setStyleSheet("background-color: white;border: 0px solid gray;border-radius:10px;color:rgb(0, 0, 0);font-size: 14px;")
        self.send_b_6.setStyleSheet(
            "background-color: transparent;border: 0px solid gray;font-size: 25px;border-radius:10px;")
        
        self.line.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.add_frindl.setStyleSheet("background-color: transparent;border: 0px solid gray;border-radius:10px;color:rgb(95, 125, 149);font-size: 15px;")
        self.add_frindl_2.setStyleSheet("background-color: transparent;border: 0px solid gray;border-radius:10px;color:rgb(95, 125, 149);font-size: 15px;")
        self.frame_2.setStyleSheet("background-color: rgba(255,255,255,.92);")
        
        


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
        self.label_background.setPixmap(QPixmap(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/background.png')))

        self.wating_l.setPixmap(QPixmap(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/background.png')))
        
        self.label_14.setStyleSheet("background-color: rgba(0,0,0,.4);border:1px rgb(0,0,0);border-radius:15px;color:white")
        

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



        self.add_freind.setStyleSheet(
                    "background-color: rgb(95, 125, 149);border: 0px solid white;border-radius:11px;color : white;font-size: 13px;")

        self.invite.setStyleSheet(
                    "background-color: rgb(95, 125, 149);border: 0px solid white;border-radius:11px;color : white;font-size: 13px;")


        self.invite_2.setStyleSheet(
                    "background-color: rgb(95, 125, 149);border: 0px solid white;border-radius:11px;color : white;font-size: 13px;")

        self.cancle_user.setStyleSheet(
        "background-color: transparent;border: 1px solid white;border-radius:15px;")

        
        # self.clear_b.setWhatsThis("lksdaf;jksnf;j")

        self.label_5.setStyleSheet("background-color: transparent;")

        self.button_record.setStyleSheet(
            "background-color: transparent;border: 1px solid white;border-radius:15px;")
        self.button_send.setStyleSheet(
            "background-color: transparent;border: 0px solid white;border-radius:15px;")

        self.send_b_11.setStyleSheet(
            "background-color: light gray;border: 0px solid white;border-radius:20px;")

        self.send_b_11.setIcon(QIcon(os.getcwd() + "/UI/Master"  +'/icons/up-chevron.png'))
        
        self.cancle_user.setIcon(QIcon(os.getcwd() + "/UI/Master"  +'/icons/left-arrow.png'))

        
        self.send_b_11.setHidden(True)
        self.button_attach.setStyleSheet(
            "background-color: transparent;border: 0px solid white;border-radius:15px;")
        self.textedit_messegebox.setStyleSheet(
            "background-color: white;border: 1px solid lightgray;border-radius:18px;font-size: 20px;")
        self.button_usersearch.setStyleSheet(
            "background-color: white;border: 1px solid white;")
        self.textedit_usersearch.setStyleSheet(
            "background-color: white;border: 1px solid gray;border-radius:15px;")



        self.usernamem_l.setStyleSheet("background-color: transparent;border: 0px solid lightgray;border-radius:1px;font-size: 15px;")
        self.lastseen_l.setStyleSheet("background-color: transparent;border: 0px solid lightgray;border-radius:1px;font-size: 12px;")
        
        

        self.button_menu_user.setIcon(
            QIcon(os.getcwd() + "/UI/Master"  +'/icons/menu_user.png'))
        self.button_searchuser.setIcon(QIcon(os.getcwd() + "/UI/Master"  +'/icons/search.png'))
        self.button_call.setIcon(QIcon(os.getcwd() + "/UI/Master"  +'/icons/phone.png'))
        self.emoji_BTN_2.setIcon(QIcon(os.getcwd() + "/UI/Master"  +'/icons/laugh2.png'))
        self.emoji_BTN.setIcon(
            QIcon(os.path.abspath(os.getcwd() + "/UI/Master"   + '/icons/laugh.png')))

        self.button_usersearch.setIcon(QIcon(os.getcwd() + "/UI/Master"  +'/icons/search.png'))
        self.button_menu.setIcon(QIcon(os.getcwd() + "/UI/Master"  +'/icons/menu.png'))
        self.button_record.setIcon(QIcon(os.getcwd() + "/UI/Master"  +'/icons/radio.png'))
        self.button_attach.setIcon(QIcon(os.getcwd() + "/UI/Master"  +'/icons/clip.png'))
        self.button_send.setIcon(QIcon(os.getcwd() + "/UI/Master"  +'/icons/send.png'))

        self.send_b_14.setIcon(QIcon(os.getcwd() + "/UI/Master"  +'/icons/add-button.png'))

        self.send_b_14.clicked.connect(self.show_add_invite)
        self.invite.clicked.connect(self.sms_invite)
        self.add_freind.clicked.connect(self.add_user_freind)

        self.user_add.setStyleSheet("background-color: white;border: 1px solid gray;border-radius:10px;")
        self.user_add_2.setStyleSheet("background-color: white;border: 1px solid gray;border-radius:10px;")

        



        self.cancle_user.clicked.connect(self.hide_add_invite)

        self.send_b_14.setStyleSheet("background-color: rgba(230, 230, 230, 0.7);border: 0px solid white;border-radius:20px;" )

        self.button_send.clicked.connect(self.clickedBtn_send)
    
        self.button_clear.clicked.connect(self.voice_mess_other)
        self.searchuser_b.clicked.connect(self.click_search)
        self.pushButton.clicked.connect(self.back_from_search)
        
        self.doc_BTN.clicked.connect(lambda:self.file_send(["d",""]))
        self.attach_b_2.clicked.connect(self.click_attach_2)
        self.camera_BTN.clicked.connect(self.click_camera_BTN)
        self.menu_b.clicked.connect(self.start_menu)

        

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

        # window.pushButton_7.setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"   + '/UI/Login/images/error.png')))
        # window.label_18.setHidden(False)
        # window.label_18.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')
        # movie = QtGui.QMovie(os.getcwd() + "/UI/Master"   + '/UI/Login/images/loading2.gif')
        # window.label_18.setMovie(movie)
        # movie.start()

        self.attach_b_2.setHidden(True)
        self.attach_b_2.setIcon(
            QIcon(os.path.abspath(os.getcwd() + "/UI/Master"   + '/icons/clip.png')))
        self.menu_bk_BTN.setIcon(
            QIcon(os.path.abspath(os.getcwd() + "/UI/Master"   + '/icons/arrow.png')))
        self.menu_bk_BTN.setStyleSheet(
            "background-color: transparent;border: 0px solid white;border-radius:15px;")

        self.scrollArea.verticalScrollBar().setStyleSheet(
            "border: none;background: lightgray;height: 26px;margin: 0px 26px 0 26px;")
        self.listWidget.verticalScrollBar().setStyleSheet(
            "border: none;background: lightgray;height: 26px;margin: 0px 26px 0 26px;")

        self.profile_LBL.setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"   + '/Files/profile/output.png')))
        self.profile_LBL.clicked.connect(self.contex_change_profile)

        self.profile_LBL.setStyleSheet("background-color: transparent;border: 0px solid white ;border-radius: 90px;")

        self.pv_LBL.setStyleSheet(
            "background-color: transparent;border: 0px solid gray ;border-radius: 20px;")
        self.pv_LBL.setIcon(
            QIcon(os.path.abspath(os.path.abspath(os.getcwd() + "/UI/Master"   + '/Files/profile/person.png'))))
        self.label_7.setStyleSheet("background-color: transparent;")
        self.label_6.setStyleSheet("background-color: transparent;")
        # self.emoji_FRM.setHidden(True)
        self.doc_BTN.setHidden(True)
        self.doc_BTN.setIcon(QIcon(os.path.abspath(
            os.getcwd() + "/UI/Master"   + '/icons/document.png')))

        self.camera_BTN.setHidden(True)
        self.camera_BTN.setIcon(
            QIcon(os.path.abspath(os.getcwd() + "/UI/Master"   + '/icons/camera.png')))

        self.record_b.setStyleSheet(
            "background-color: transparent;border: 0px solid gray ;border-radius: 20px;")
        self.record_b.setIcon(
            QIcon(QPixmap(os.path.abspath(os.getcwd() + "/UI/Master"   + '/icons/radio.png'))))

        self.send_b_13.setStyleSheet(
            "background-color: transparent;border: 0px solid gray ;border-radius: 20px;")
        self.send_b_13.setIcon(
            QIcon(QPixmap(os.path.abspath(os.getcwd() + "/UI/Master"   + '/icons/close (1).png'))))
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

        self.send_b_6.setToolTip("<font color=white>%s</font>" % '🌹'.replace("\n", "<br/>"))
        self.send_b_3.setToolTip("<font color=white>%s</font>" % '😬'.replace("\n", "<br/>"))
        self.send_b_2.setToolTip("<font color=white>%s</font>" % '🙏'.replace("\n", "<br/>"))
        self.send_b_5.setToolTip("<font color=white>%s</font>" % '💪'.replace("\n", "<br/>"))
        self.send_b_4.setToolTip("<font color=white>%s</font>" % '👋'.replace("\n", "<br/>"))
        self.send_b_10.setToolTip("<font color=white>%s</font>" % '👍'.replace("\n", "<br/>"))
        self.send_b_9.setToolTip("<font color=white>%s</font>" % '👌'.replace("\n", "<br/>"))
        self.send_b_8.setToolTip("<font color=white>%s</font>" % '🥰'.replace("\n", "<br/>"))
        self.send_b_7.setToolTip("<font color=white>%s</font>" % '🖐'.replace("\n", "<br/>"))
        self.send_b_12.setToolTip("<font color=white>%s</font>" % '💋'.replace("\n", "<br/>"))

        self.send_b_14.setToolTip("<font color=black>%s</font>" % 'Add'.replace("\n", "<br/>"))
        self.cancle_user.setToolTip("<font color=white>%s</font>" % 'Go Back'.replace("\n", "<br/>"))
        self.add_freind.setToolTip("<font color=white>%s</font>" % 'Add'.replace("\n", "<br/>"))
        self.invite.setToolTip("<font color=white>%s</font>" % 'Send Sms'.replace("\n", "<br/>"))
        self.invite_2.setToolTip("<font color=black>%s</font>" % 'Qr Code'.replace("\n", "<br/>"))
        
        

        self.menu_user_b.clicked.connect(self.contex_menu)
        self.invite_2.clicked.connect(self.qr_invite)
        

        self.emoji_BTN_2.setEnabled(True)
        self.emoji_BTN_2.setHidden(True)
            

        self.emoji_FRM.setHidden(True)
        self.label_8.setHidden(True)
        self.label_9.setHidden(True)

        # self.textedit_messegebox.setHidden(True)
        # self.label.setHidden(True)
        # self.label.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')

        # movie = QtGui.QMovie(os.getcwd() + "/UI/Master"   + '/icons/floding.gif')
        # print(os.getcwd() + "/UI/Master"   + '/icons/floading.gif')
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
        global new_messeg
        self.timer19 = QtCore.QTimer()
        self.timer19.timeout.connect(lambda : self.choos_type(new_messeg))
        self.timer19.start(1)
        
        # 
   
        self.center()

        
        self.show()

    def sms_invite(self):
        if  self.user_add_2.text() :
            try:
                api = KavenegarAPI('6A7654584E6D34646A486137726D5A586858695A655A464566566D7A6D683331626B4E33394D594B7835493D')
                params = {
                    'sender': '10004346',
                    'receptor': str(self.user_add_2.text()),
                    'message': 'Lets Chat On PyChat.'
                            }   
                response = api.sms_send(params)
                QMessageBox.about(self, "PyChat", "Invitation message sent successfully")
                self.hide_add_invite()
            except : 
                QMessageBox.about(self, "PyChat", "ooops! Try Again Later.")
        else:
            QMessageBox.about(self, "PyChat", "Please enter phonenumber.")

        
        
    def add_user_freind(self):
        if  self.user_add.text() :
            pass
        else:
            QMessageBox.about(self, "PyChat", "Please enter User Name.")


    def choos_type(self,data):
        if data==[]:
            return

        elif data[0] == 't':
            self.clickedBtn_other(data[1:])

        elif data[0] == 'm':
            self.file_receve(data[1:])

        
    def user_list_click(self,item):
        global reciver
        reciver = item.text().strip('\n').lstrip()
        self.pv_LBL.setIcon(item.icon())

        self.usernamem_l.setText(item.text().strip('\n').lstrip())
        # print(item.whatsThis())
        self.wating_l.setHidden(True)
        self.label_14.setHidden(True)
 
    def contex_change_profile(self):
        menu = QMenu(self)
        View = newAct = menu.addAction("View photo")
        Take = menu.addAction("Take photo")
        Upload = menu.addAction("Upload photo")
        avatar = menu.addAction("choose avatar")
        Remove = menu.addAction("Remove photo")
        

        View.triggered.connect(self.show_profile_pic)
        Take.triggered.connect(self.capture_pic_profile)
        Upload.triggered.connect(self.choose_profile_pic)
        avatar.triggered.connect(self.avatar)
        Remove.triggered.connect(self.delete_profile_pic)
        menu.exec_(QCursor.pos())
    
    def hide_add_invite(self):
        self.frame_2.setGeometry(QtCore.QRect(0, 800, 321, 361))
        self.user_add_2.clear()
        self.user_add.clear()
        # self.listWidget.setEnabled(True)


    def show_add_invite(self):
        self.frame_2.setGeometry(QtCore.QRect(60, 210, 321, 361))

        # self.listWidget.setEnabled(False)

    def qr_invite(self):
        global token
        if self.user_add_2.text() :
        
            s = "SMSTO:"+str(self.user_add_2.text())+":"+token+" invited you to chat on PyChat.\n\nYou can download PyChat with the link below : \n\nbit.ly/2CCrEQH"
            url = pyqrcode.create(s)
            
            url.png(os.getcwd() + "/UI/Master"  +'/icons/invite.png', scale = 6)
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, os.getcwd() + "/UI/Master"  +'/icons/invite.png'])
            self.hide_add_invite()
        else:
            QMessageBox.about(self, "PyChat", "Please enter phonenumber.")

    def avatar (self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', os.path.abspath(os.getcwd() + "/UI/Master/Files/avatar/") ,"Image files (*.jpg *.png)")
        except FileNotFoundError:
            print("c")
            return
        dst = os.path.abspath(os.getcwd() + "/UI/Master"   + '/Files/profile/output.png')
       
        shutil.copy(fname[0], dst)
        #circle pic
        size = (500, 500)
        from PIL import Image, ImageOps, ImageDraw
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + size, fill=255)
        from PIL import ImageFilter
        im = Image.open(os.path.abspath(os.getcwd() + "/UI/Master"  +'/Files/profile/output.png'))
        output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)
        output.save(os.path.abspath(os.getcwd() + "/UI/Master"  +'/Files/profile/output.png'))

        self.profile_LBL.setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"   + '/Files/profile/output.png')))

    def delete_profile_pic(self):
        qm = QMessageBox()
        ret = qm.question(self,'warning!', "Are you sure you want to delete your profile picture?", qm.Yes | qm.No)
        if ret == qm.Yes:
            src = os.path.abspath(os.getcwd() + "/UI/Master"   + '/icons/output.png')
            dst = os.path.abspath(os.getcwd() + "/UI/Master"   + '/Files/profile/output.png')
            shutil.copy(src, dst)
            self.profile_LBL.setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"   + '/Files/profile/output.png')))
        else:
            pass
        
    def show_profile_pic(self):
        from PIL import Image, ImageOps, ImageDraw
        

        img = Image.open(os.path.abspath(os.getcwd() + "/UI/Master"   + '/Files/profile/output.png'))
        defult = Image.open(os.path.abspath(os.getcwd() + "/UI/Master"   + '/icons/output.png'))

        if defult.histogram() == img.histogram(): 
            QMessageBox.about(self, "PyChat", "You do not have a profile picture to display")
            
        else:
            img.show()
            
    def choose_profile_pic(self):
        from PIL import Image, ImageOps, ImageDraw
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.png)")
        except FileNotFoundError:
            return
        dst = os.path.abspath(os.getcwd() + "/UI/Master"   + '/Files/profile/output.png')
       
        shutil.copy(fname[0], dst)
        #circle pic
        size = (500, 500)
        
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + size, fill=255)
        from PIL import ImageFilter
        im = Image.open(os.path.abspath(os.getcwd() + "/UI/Master"  +'/Files/profile/output.png'))
        output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)
        output.save(os.path.abspath(os.getcwd() + "/UI/Master"  +'/Files/profile/output.png'))

        self.profile_LBL.setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"   + '/Files/profile/output.png')))
        
    def capture_pic_profile(self):
        from PIL import Image, ImageOps, ImageDraw
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
                img_name = os.path.abspath(os.getcwd() + "/UI/Master"   + '/Files/profile/output.png')
                cv2.imwrite(img_name, frame)
                
                #circle pic
                size = (500, 500)
                mask = Image.new('L', size, 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0) + size, fill=255)
                from PIL import ImageFilter
                im = Image.open(os.path.abspath(os.getcwd() + "/UI/Master"  +'/Files/profile/output.png'))
                output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
                output.putalpha(mask)
                output.save(os.path.abspath(os.getcwd() + "/UI/Master"  +'/Files/profile/output.png'))
                cam.release()
                cv2.destroyAllWindows()
                self.profile_LBL.setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"   + '/Files/profile/output.png')))


               

        cam.release()

        cv2.destroyAllWindows()

    def download_state(self,data):
        global download_status
        where = self.index_serarch(data[0])
        if where == -1 :
            return
        print(where,type(where))

        if download_status == True:
           
            if os.path.splitext(data[0])[1] in ['.jpg','.png','.jpeg']:
                self.formLayout.itemAt(where).widget().setIcon(QIcon(os.path.abspath(os.getcwd()+'/'+data[0])))
                self.formLayout.itemAt(where).widget().setIconSize(QSize(500, 300))

            elif os.path.splitext(data[0])[1] in ['.mkv','.mp4']:
                self.formLayout.itemAt(where).widget().setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/video-camera.png')))
                self.formLayout.itemAt(where).widget().setIconSize(QSize(300, 35))

            elif os.path.splitext(data[0])[1] in ['.mp3','.vaw']:
                self.formLayout.itemAt(where).widget().setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/mp3.png')))
                self.formLayout.itemAt(where).widget().setIconSize(QSize(300, 35))

            else:
                self.formLayout.itemAt(where).widget().setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/file.png')))
                self.formLayout.itemAt(where).widget().setIconSize(QSize(300, 35))


            self.formLayout.itemAt(where).widget().setStyleSheet("background-color: white;border: 8px solid white;border-radius: 25px;font-size: 20px;")
            
            download_status=False
            print(download_status)
            self.timer17.stop()
        else:
            self.formLayout.itemAt(where).widget().setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/download (1).png')))

 
    def download_file(self,data):
       
        if os.path.isfile(data[0]):
            file =os.path.abspath(os.getcwd()+'/'+data[0])
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, file])
        else:
            
            
            self.timer17 = QtCore.QTimer()
            self.timer17.timeout.connect(lambda :self.download_state(data))
            self.timer17.start(200)
            
            sending_to_server(s,[int(120),data[0]])
    
    def index_serarch(self,txt): ########################################################################################
        for i in range(0,self.formLayout.count()-1):
            
            if str(self.formLayout.itemAt(i).widget().whatsThis()) == str(txt):
                print(i)
                return i
        return -1
    
    def file_receve(self,data):
        global new_messeg

        if self.scrollArea.verticalScrollBar().value() == self.scrollArea.verticalScrollBar().maximum():
            QTimer.singleShot(50, self.scrol_down)
        self.user_image = QPushButton()
        self.user_image.setIcon(
            QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/user.png')))
        self.user_image.setIconSize(QSize(35, 35))

        self.messege_user = QPushButton()
        self.messege_user.setIcon(
            QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/download.png')))
            
        self.messege_user.setIconSize(QSize(300, 35))

        # self.messege_user.setStyleSheet("background-color: white;border: 1px solid lightgray;border-radius: 17px;font-size: 20px;")
        if self.last_used == "me":
            self.formLayout.addRow(QLabel())
        self.formLayout.addRow(self.user_image, self.messege_user)
        self.formLayout.itemAt(self.formLayout.count()-2).widget().clicked.connect(self.clickedBtn_user)

        self.formLayout.itemAt(self.formLayout.count()-2).widget().setStyleSheet(
            "background-color:transparent;border: 0px solid white;border-radius:20px;color:white;")
        self.formLayout.itemAt(self.formLayout.count(
        )-2).widget().setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.formLayout.itemAt(self.formLayout.count()-1).widget().clicked.connect(lambda : self.download_file (data))
        self.formLayout.itemAt(self.formLayout.count()-1).widget().setWhatsThis(data[0])

        self.formLayout.itemAt(self.formLayout.count()-1).widget().setStyleSheet(
            "background-color: white;border: 8px solid white;border-radius: 25px;font-size: 20px;")
        self.formLayout.itemAt(self.formLayout.count(
        )-1).widget().setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.messege_time = QLabel(datetime.datetime.now().strftime(
            "%H:%M"), alignment=Qt.AlignRight)
        self.messege_time.setStyleSheet("color: black")
        self.messege_time.setStyleSheet(
            "background-color: transparent;border: 0px solid lightgray;border-radius: 5px;font-size: 14px;")
        self.id = QLabel('')
        # self.seen_image.setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/reply.png')))
        self.id.setStyleSheet(
            "background-color: transparent;border: 0px none;border-radius: 10px;font-size: 1px;")

        self.formLayout.addRow(self.id, self.messege_time)
        self.last_used = "other"
        new_messeg.clear()

    def file_s_open(self,patch):
        global download_status
        where = self.index_serarch(patch)
        if where == -1 :
            return

        if os.path.isfile(patch):
           
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, patch])
        # print(where,type(where))
        
        
        

        

    def file_send(self,wich):
        global token,reciver
        self.attach_b.setHidden(False)
        self.attach_b_2.setHidden(True)
        self.timer12 = QtCore.QTimer()
        self.timer12.timeout.connect(self.doc_movedown)
        self.timer12.start(5)
        global token,reciver
        fname=[]
        if wich[0]=='c':
            print(wich[1])
            fname=[wich[1],'']

        else:
            try:
                fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"All files *.*")
            except FileNotFoundError:
                return 0
        obj.send_file(s,token,reciver,'m',fname[0])
        self.exit_emoji_box()

        if self.scrollArea.verticalScrollBar().value() == self.scrollArea.verticalScrollBar().maximum():
            QTimer.singleShot(50, self.scrol_down)
        self.user_image = QPushButton()
        self.user_image.setIcon(
            QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/me.png')))
        self.user_image.setIconSize(QSize(35, 35))

        self.messege_user = QPushButton()


        self.messege_user.setIcon(QIcon(fname[0]))
            
        self.messege_user.setIconSize(QSize(500, 300))

        # self.messege_user.setStyleSheet("background-color: white;border: 0px solid lightgray;border-radius: 17px;font-size: 20px;")
        if self.last_used == "me":
            self.formLayout.addRow(QLabel())
        self.formLayout.addRow(self.user_image, self.messege_user)
        self.formLayout.itemAt(self.formLayout.count()-2).widget().clicked.connect(self.clickedBtn_user)

        self.formLayout.itemAt(self.formLayout.count()-2).widget().setStyleSheet(
            "background-color:transparent;border: 0px solid white;border-radius:20px;color:white;")
        self.formLayout.itemAt(self.formLayout.count(
        )-2).widget().setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.formLayout.itemAt(self.formLayout.count()-1).widget().clicked.connect(lambda : self.file_s_open (fname[0]))
        self.formLayout.itemAt(self.formLayout.count()-1).widget().setWhatsThis(fname[0])

        self.formLayout.itemAt(self.formLayout.count()-1).widget().setStyleSheet(
            "background-color: #D7FAB3;border: 12px solid rbg(215,250,175);border-radius: 25px;font-size: 20px;")
        self.formLayout.itemAt(self.formLayout.count(
        )-1).widget().setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        where = self.formLayout.count()-1

        if os.path.splitext(fname[0])[1] in ['.jpg','.png','.jpeg']:
            self.formLayout.itemAt(where).widget().setIcon(QIcon(fname[0]))
            self.formLayout.itemAt(where).widget().setIconSize(QSize(500, 300))

        elif os.path.splitext(fname[0])[1] in ['.mkv','.mp4']:
            self.formLayout.itemAt(where).widget().setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/video-camera.png')))
            self.formLayout.itemAt(where).widget().setIconSize(QSize(300, 35))

        elif os.path.splitext(fname[0])[1] in ['.mp3','.vaw']:
            self.formLayout.itemAt(where).widget().setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/mp3.png')))
            self.formLayout.itemAt(where).widget().setIconSize(QSize(300, 35))

        else:
            self.formLayout.itemAt(where).widget().setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/file.png')))
            self.formLayout.itemAt(where).widget().setIconSize(QSize(300, 35))



        self.messege_time = QLabel(" 12:54 ", alignment=Qt.AlignRight)
        self.messege_time.setStyleSheet("color: black")
        self.messege_time.setStyleSheet(
            "background-color: white;border: 0px solid lightgray;border-radius: 5px;font-size: 14px;")
        self.seen_image = QLabel()
        self.seen_image.setPixmap(QPixmap(os.path.abspath(
            os.getcwd() + "/UI/Master"  +'/icons/not_seen.png')).scaledToWidth(20))
        self.formLayout.addRow(self.messege_time, self.seen_image)
        self.last_used = "other"
        new_messeg.clear()

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
            "background-color: transparent;border: 0px solid white ;border-radius: %dpx;" % int(zoom_smth/2))
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
        movie = QtGui.QMovie(os.getcwd() + "/UI/Master"   + '/icons/rec_button.gif')
        self.record_b.setIcon(
            QIcon(QPixmap(os.path.abspath(os.getcwd() + "/UI/Master"   + '/icons/radio.png'))))
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
            os.getcwd() + "/UI/Master"   + '/icons/ezgif.com-gif-maker (5).gif')
        self.label_8.setMovie(movie)
        movie.start()
        QTimer.singleShot(2000, lambda: self.label_8.setHidden(True))
        QTimer.singleShot(2000, self.deleting_gif)
        # self.messegebox_t.resize(571, 31)

        self.send_b_13.setHidden(True)

    def start_rec_voice(self):
       
        filename = os.getcwd() + "/UI/Master"  +'/Files/'+'1.wav'
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
      
        thread = threading.Thread(target=lambda : playsound(os.getcwd() + "/UI/Master"  +'/Files/'+voice_id) )
        thread.start()
    
        self.timer50 = QtCore.QTimer()
        self.timer50.timeout.connect(lambda : self.slider_over(itm,play_t))
        self.timer50.start(1000)
        
        # print(mediainfo(os.getcwd() + "/UI/Master"  +'/Files/'+voice_id)['duration'])
     
    def rec_voice(self):
        global record_until
        self.exit_emoji_box()
        if self.record_b.isChecked():

            record_until = False
            self.voice_mess_me("1.wav")
            self.label_9.setHidden(False)
            movie = QtGui.QMovie(os.getcwd() + "/UI/Master"   + '/icons/sendmic.gif')
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
                QIcon(QPixmap(os.path.abspath(os.getcwd() + "/UI/Master"   + '/icons/radio.png'))))
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
            movie = QtGui.QMovie(os.getcwd() + "/UI/Master"   + '/icons/rec_button.gif')
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
            movie = QtGui.QMovie(os.getcwd() + "/UI/Master"   + '/icons/rec_button.gif')
            self.label_7.setMovie(movie)
            movie.start()

            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.rec_sec)
            self.timer.start(1000)
            # self.timer22 = QtCore.QTimer()
            # self.timer22.timeout.connect(self.cheack_port)
            # self.timer22.start(1000)
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
                QIcon(QPixmap(os.path.abspath(os.getcwd() + "/UI/Master"   + '/icons/correct.png'))))
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
            "background-color: transparent;border: 0px solid white ;border-radius: %dpx;" % int(zoom_smth/2))
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
        from PIL import Image, ImageOps, ImageDraw
        QMessageBox.about(self, "Hint", "press space to capture picture or esc to quit")
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("send Pic")
        while True:
            ret, frame = cam.read()
            if not ret:
                break
            cv2.imshow("send Pic", frame)
            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = os.path.abspath(os.getcwd() + "/UI/Master"   + '/Files/camera/output.png')
                cv2.imwrite(img_name, frame)
                cam.release()
                cv2.destroyAllWindows()
                self.file_send(["c",os.getcwd() + "/UI/Master"   + '/Files/camera/output.png'])

            
        
           
           


               

        cam.release()

        cv2.destroyAllWindows()

        

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
            QIcon(os.path.abspath(os.getcwd() + "/UI/Master"   + '/icons/search.png')))

        self.pushButton.setHidden(False)
        self.pushButton.setIcon(
            QIcon(os.path.abspath(os.getcwd() + "/UI/Master"   + '/icons/back.png')))

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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            # self.close()
            # self.clickedBtn_send()
            pass

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
        global token,reciver
        self.exit_emoji_box()
        obj.send_text_message(s,token,reciver,self.textedit_messegebox.toPlainText())
        if self.scrollArea.verticalScrollBar().value() == self.scrollArea.verticalScrollBar().maximum():
            QTimer.singleShot(50, self.scrol_down)
        if self.textedit_messegebox.toPlainText().strip():
            massege_text = "\n   "
            self.user_image = QPushButton()
            self.user_image.setIcon(
                QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/me.png')))
            self.user_image.setIconSize(QSize(35, 35))

            if len(self.textedit_messegebox.toPlainText().strip()) <= 66:
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
                os.getcwd() + "/UI/Master"  +'/icons/not_seen.png')).scaledToWidth(20))
            self.formLayout.addRow(self.messege_time, self.seen_image)
            self.last_used = "me"
            
            

    def clickedBtn_other(self,data):

        global new_messeg
  
        time_2 = data[1]
        time_2=time_2[11:16]
        messege = data[0]

        if self.scrollArea.verticalScrollBar().value() == self.scrollArea.verticalScrollBar().maximum():
            QTimer.singleShot(50, self.scrol_down)
        self.user_image = QPushButton()
        self.user_image.setIcon(
            QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/user.png')))
        self.user_image.setIconSize(QSize(35, 35))
        # self.user_image.setPixmap(QPixmap(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/user.png')).scaledToWidth(35))
        self.messege_user = QLabel(messege)
        self.messege_user.setStyleSheet(
            "background-color: white;border: 1px solid lightgray;border-radius: 17px;font-size: 20px;")
        if self.last_used == "me":
            self.formLayout.addRow(QLabel())
        self.formLayout.addRow(self.user_image, self.messege_user)
       
        self.formLayout.itemAt(self.formLayout.count()-2).widget().setWhatsThis(messege)

        self.formLayout.itemAt(self.formLayout.count()-2).widget().clicked.connect(self.clickedBtn_user)

        self.formLayout.itemAt(self.formLayout.count()-2).widget().setStyleSheet(
            "background-color:transparent;border: 0px solid white;border-radius:20px;color:white;")
        self.formLayout.itemAt(self.formLayout.count()-2).widget().setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.messege_time = QLabel(time_2, alignment=Qt.AlignRight)
        self.messege_time.setStyleSheet("color: black")
        self.messege_time.setStyleSheet(
            "background-color: transparent;border: 0px solid lightgray;border-radius: 5px;font-size: 14px;")
        self.seen_image = QPushButton()
        # self.seen_image.setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/reply.png')))
        self.seen_image.setStyleSheet(
            "background-color: transparent;border: 0px solid white;border-radius: 10px;")
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight)
        self.formLayout.addRow(self.seen_image, self.messege_time)
        self.last_used = "other"
        new_messeg.clear()

    def voice_mess_other(self):
        self.formLayout.addRow(QLabel())
        if self.scrollArea.verticalScrollBar().value() == self.scrollArea.verticalScrollBar().maximum():
            QTimer.singleShot(50, self.scrol_down)
        self.user_image = QPushButton()
        self.user_image.setIcon(
            QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/user.png')))
        self.user_image.setIconSize(QSize(35, 35))
        if self.last_used == "me":
            self.formLayout.addRow(QLabel())
        self.seen_image = QPushButton()
        self.seen_image.setIcon(
            QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/google-play.png')))
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
            QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/me.png')))
        self.user_image.setIconSize(QSize(35, 35))
        if self.last_used == "other":
            self.formLayout.addRow(QLabel())
        self.seen_image = QPushButton()
        self.seen_image.setIcon(
            QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/google-play.png')))
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
        self.voice.setMaximum(int(abs(float(mediainfo(os.getcwd() + "/UI/Master"  +'/Files/'+connect_to)['duration']))))
        ##
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight)
        self.formLayout.addRow(self.messege_time, self.voice)

        self.formLayout.itemAt(self.formLayout.count()-3).widget().clicked.connect(lambda : self.play_voice(connect_to,self.formLayout.count()-3,int(abs(float(mediainfo(os.getcwd() + "/UI/Master"  +'/Files/'+connect_to)['duration'])))) )


        self.formLayout.itemAt(self.formLayout.count(
        )-1).widget().sliderReleased.connect(self.clickedBtn_user)

        self.formLayout.addRow(QLabel())
        self.formLayout.addRow(QLabel())
        self.last_used = "me"

    def clickedBtn_user(self):
    
        itm = QListWidgetItem("\nyasin78\n")
        itm.setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/user.png')))
        self.listWidget.insertItem(0,itm)
        itm = QListWidgetItem("\nmhfa1380\n")
        itm.setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/me.png')))
        self.listWidget.insertItem(1,itm)
        itm = QListWidgetItem("\n Mohammad Hossein Fadavi \n")
        itm.setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/person.png')))
        self.listWidget.insertItem(2,itm)
        itm = QListWidgetItem("\n Mostafa Bastam \n")
        itm.setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/woman.png')))
        self.listWidget.insertItem(3,itm)
        
        self.listWidget.item(0).setWhatsThis('0')
        self.listWidget.item(1).setWhatsThis('1')
        self.listWidget.item(2).setWhatsThis('2')

        # self.listWidget.item(1).setForeground(QtCore.Qt.blue)
        # self.listWidget.item(1).setIcon(QIcon(os.path.abspath(os.getcwd() + "/UI/Master"  +'/icons/me.png')))
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
    

class face_ui(QMainWindow):
    
    def __init__(self):

        self.close_cam = False
        super(face_ui, self).__init__()
        uic.loadUi(os.getcwd()+"/UI/Unlock/unlock.ui", self)

        self.setStyleSheet("QWidget { background-color: %s}" %
                           QtGui.QColor(247, 247, 247).name())

        self.welcome_l.setHidden(True)
        self.offset = None
        radius = 25.0
        path = QtGui.QPainterPath()
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)

        # self.lookingfor_l.setHidden(False)
        self.lookingfor_l.setStyleSheet(
            'background-color:rgba(255, 255, 255, 0.5);')

        movie = QtGui.QMovie(os.getcwd() + '/UI/Unlock/befor.gif')
        self.lookingfor_l.setMovie(movie)
        movie.start()

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.textEdit.setStyleSheet(
            "background-color:  rgb(247, 247, 247);border: 1px solid rgb(0, 0, 0);border-radius:15px;color:black;")

        self.move(qr.topLeft())
        self.welcome_l.setStyleSheet(
            'background-color:transparent;color:rgb(107, 107, 107)')
        self.welcome_l_2.setStyleSheet(
            'background-color:transparent;color:rgb(107, 107, 107)')

        self.textEdit.textChanged.connect(self.textChanged_messege_event)
        self.show()
        self.face_id_unlock()

    def textChanged_messege_event(self):
        if str(self.textEdit.text()) == '1234':
            self.close_cam = True
            self.show_next()
            self.welcome_l_2.setHidden(True)
            self.textEdit.setHidden(True)

    def face_id_unlock(self):
        app_face.processEvents()
        face_count = 0
        video_capture = cv2.VideoCapture(0)
        # Load a sample picture and learn how to recognize it.
        obama_image = face_recognition.load_image_file(os.getcwd() + "/UI/Unlock/face.jpg")
        app_face.processEvents()
        obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
        known_face_encodings = [obama_face_encoding, ]
        known_face_names = ["Mohammad Hossein", ]
        face_locations = []
        face_encodings = []
        app_face.processEvents()
        face_names = []
        process_this_frame = True
        while True:
            app_face.processEvents()
            ret, frame = video_capture.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            if process_this_frame:
                face_locations = face_recognition.face_locations(
                    rgb_small_frame)
                face_encodings = face_recognition.face_encodings(
                    rgb_small_frame, face_locations)
                face_names = []
                for face_encoding in face_encodings:
                    app_face.processEvents()
                    matches = face_recognition.compare_faces(
                        known_face_encodings, face_encoding)
                    name = "Unknown"
                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]
                    face_names.append(name)

            process_this_frame = not process_this_frame

            print('\033c')
            print(face_count)

            if face_names == known_face_names:
                app_face.processEvents()
                face_count += 1
            else:
                face_count = 0
            if face_count == 30 or self.close_cam == True:
                break

        # Release handle to the webcam
        app_face.processEvents()
        video_capture.release()
        cv2.destroyAllWindows()
        self.close_cam = True
        self.show_next()

    def show_next(self):

        if self.close_cam == True:

            self.lookingfor_l.setStyleSheet(
                'background-color:rgba(255, 255, 255, 0.5);')
            movie = QtGui.QMovie(os.getcwd() + '/UI/Unlock/after.gif')
            self.lookingfor_l.setMovie(movie)
            movie.start()
            self.welcome_l.setText("Hello "+"mohammad hossein"+" !")
            self.welcome_l_2.setHidden(True)
            self.textEdit.setHidden(True)
            self.welcome_l.setHidden(False)

            self.timer_face = QtCore.QTimer()
            self.timer_face.singleShot(3400, lambda: self.close())


app_face = QApplication(sys.argv)
face = face_ui()
app_face.exit(app_face.exec_())

App = QApplication(sys.argv)
window2 = UI_Master()
sys.exit(App.exec_())




if (path.isfile('Other/lice_l_2.txt')):

    app_face = QApplication(sys.argv)
    face = face_ui()
    app_face.exit(app_face.exec_())
    pass
else:
    app = QApplication(sys.argv)
    window = UI_Ads()
    app.exec_()

