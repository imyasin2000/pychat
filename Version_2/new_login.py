import socket
import subprocess
import json
from queue import Queue 
import threading
from PyQt5 import QtCore, QtGui, QtWidgets #works for pyqt5
import time
from select import select
from PyQt5.QtWidgets import * #UI
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

from requests import get, post
import json
import webbrowser
import jwt
import base64
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import urllib.request


q=Queue()
s=socket.socket()

#Server information
## 51.195.19.3
s.connect(('0.0.0.0',1237))

email_changer=''
data_user=[]
code_g=0

class user :
    def __init__ (self):
        pass
    #ersal etelaat karbar jadid be samte server 
    def login(self,s:socket,capcha_code):
        global window
        self.data=[int(100)]
        self.username=window.lineEdit_user.text()
        self.name=window.lineEdit_name.text()
        self.email=window.lineEdit_email.text()
        #cheak email is valid

        if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', self.email)):

            self.password = window.lineEdit_pass.text()
            self.capcha_label = window.lineEdit_capcha.text()
            to_chek_password = window.lineEdit_repass.text()
            if self.cheking_password(self.password, to_chek_password):
                self.data.append(self.username)
                self.data.append(self.name)
                self.data.append(self.email)
                hashedpass = hashlib.md5(self.password.encode()).hexdigest()
                hashedpass=hashedpass[0:-5] + hashedpass[5:-8]
                self.data.append(hashedpass)
                if self.capcha_label==str(capcha_code):
                    sending_to_server(s, self.data)
                    wating_form(True,"forget_e")
                else:
                    QMessageBox.about(window, "recapcha error", "capcha code is not true")
                    window.lineEdit.setFocus()
            else:
                window.lineEdit.clear()
                QMessageBox.about(window, "password error", "oh! try agian to enter password because they are not equal!")
                window.Username_LE_7.clear()
                window.Username_LE_7.setFocus()
        else:
            QMessageBox.about(window, "Invalid Email","enter valid email")
            window.Usename_LE_3.clear()
            window.Usename_LE_3.setFocus()
            window.lineEdit.clear()

    #tabe baraye chek kardan motabegh budan password
    def cheking_password(self,pass1,pass2):
        if pass1==pass2:
            return True
        else:
            return False
    def get_code_server_rigister(self,s:socket,data:list):
        global code_g
        global data_user
        global window
        window.Username_LE_16.clear()
        window.Username_LE_16.setFocus()
        time.sleep(2)
        wating_form(False,"")
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
        if  window.lineEdit_code_signup.text() == str(code_g):
            wating_form(True,"signup_f")
            self.data1 = [int(102)] + data_user
            sending_to_server(s, self.data1)
        else:
            window.Username_LE_16.clear()
            window.Username_LE_16.setFocus()
            QMessageBox.about(window, "Invalid Code","Code is not correct")


    #     # pasokh server be inke aya ba movafaghiat user jadid ra
    #     # be data base ezafe karde ya kheir
    def server_added_user_to_database(self,s:socket,data:list):
        # self.meesege_box(data[0])
        global window
        # QMessageBox.about(window, "My box", "hi")
        if data[0]=="welcome to pychat !":
            time.sleep(7)
            wating_form(False,"")
            window.Signup_FRM.setGeometry(QtCore.QRect(22000, 0, 801, 541))
            window.Signin_FRM.setGeometry(QtCore.QRect(0, 0, 801, 541))
            window.Recover_FRM_4.setGeometry(QtCore.QRect(22000, 0, 801, 541))
            window.Username_LE.clear()
            window.Password_LE.clear()
            window.Username_LE.setFocus()
        time.sleep(1)
        wating_form(False,"")
        notification(data[0])

    def user_want_sign_in(self,s:socket):
        global window
        self.data=[int(103)]
        self.username=window.lineEdit_username.text()
        self.data.append(self.username)
        self.password=window.lineEdit_password.text()
        hashedpass = hashlib.md5(self.password.encode()).hexdigest()
        hashedpass = hashedpass[0:-5] + hashedpass[5:-8]
        self.data.append(hashedpass)
        sending_to_server(s,self.data)



    def forgot_password(self,s:socket):
        global window
        global email_changer
        self.eemail = window.lineEdit_forgetemail.text()
        if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', self.eemail)):
            email_changer = self.eemail
            data = [int(101), 'forgot', '_', self.eemail]
            sending_to_server(s, data)
            wating_form(True,"forget_e")
        else:
            QMessageBox.about(window, "Invalid Email", "enter valid email")
            window.Username_LE_2.clear()
            window.Username_LE_2.setFocus()


    def get_code_server(self,s:socket,data:list):
        global code_g
        global window
        code_g = data[-1]
        print(code_g)
        window.Recover_FRM.setGeometry(QtCore.QRect(-3000, 0, 801, 541))
        window.Recover_FRM_2.setGeometry(QtCore.QRect(0, 0, 801, 541))
        window.Username_LE_4.setText(window.Username_LE_2.text())
        wating_form(False,"")
        window.Username_LE_3.clear()
        window.Username_LE_3.setFocus()

    def change_pass(self):
        global window
        global email_changer
        pas = window.lineEdit_forget_pass.text()
        pas2 = window.lineEdit_forget_repass.text()
        if self.cheking_password(pas, pas2) and pas!='':
            hashedpass = hashlib.md5(pas.encode()).hexdigest()
            hashedpass = hashedpass[0:-5] + hashedpass[5:-8]
            data1 = [int(107), email_changer, hashedpass]
            sending_to_server(s, data1)
            wating_form(True,"signup_e")
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
            QMessageBox.about(window, "Invalid Code","Code is not correct")


    def password_changed(self,s:socket,data:list):
        global window
        time.sleep(3)
        wating_form(False,"")
        window.Recover_FRM_3.setGeometry(QtCore.QRect(4555000, 4000, 801, 541))
        window.Signin_FRM.setGeometry(QtCore.QRect(0, 0, 801, 541))
        window.Username_LE.clear()
        window.Password_LE.clear()
        window.Username_LE.setFocus()
        notification(str(data[0]))

#----------------------------------------------------------------------------------------------other func ------------------
def wating_form(wating_until,form):
    global window
    if(wating_until):
        if cheak_net()== False:
            window.pushButton_7.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/error.png')))
            window.label_18.setHidden(False)
            window.label_18.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')
            movie = QtGui.QMovie(os.getcwd() + '/UI/Login/images/conection2.gif')
            window.label_18.setMovie(movie)
            movie.start()
            threading.Thread(target=window.net_conncted, args=()).start()
        elif form=='signin':
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

#----------------network connections with Queue--------------------------------

#in tabe tamame dade haye vorude be barname ra misanjad agar daraye etebar bashad 
#an hara accsept  mikonad
def _accsepting(s:socket):
    data = b''
    while True:
        time.sleep(0.02)
        try:
            #do taye dg niaz nabod
            r, _, _ = select([s], [s], [])#baresi mishe vasl hast ya na
            if r:
                d = s.recv(4096)
                data += d
                if len(d) < 4096:
                    if data:
                        d = data.split(b'\0')
                        #extera baraye dycrypt ezafe beshe
                        #load_data(decrypt(d[i]))
                        for i in range(len(d) - 1):
                            load_data(d[i])
                            data = d[-1]
                    else:
                        s.close()
        except:
                print("connection failed ...")
                return

#in tabe vorudi haue ghbel pardazesh ke az tabee marhale 
#ghabl amade ra decode mikonad va zemnan az halat json kharej 
#mikonad va an ha ra darun q put mikonad 
def load_data(data):
    x=(json.loads(data.decode()))
    q.put(x)

#ba farakhani in tabe har data ghbel fahm baraye server ra ersal 
#mikonim  in tabee khodkar tamame vorudi ash ra be json tablil karde
# va baad an ra ra encode mikond va ersal be server
#vorudi in tabe sheye s hast ke bala az ruye socket sakhtim
def sending_to_server(socket:socket,data):
        data=json.dumps(data)
        socket.send((data.encode()+ b'\0'))
#in tabe kar ha va darkhast hayie ke az samte server amade ra inja ejra mikonad
def do_work(obj:user,s:socket):
    while True:
        time.sleep(0.03)
        if not q.empty():
            new_data=q.get()
            task=new_data[0]
            obj_work[f"{task}"](s,new_data[1:])
            q.task_done()


obj=user()
obj_work={ 'token':"yasin78",
      '500':obj.get_code_server_rigister,
      '502':obj.server_added_user_to_database,
      '509':obj.get_code_server,
      '504':obj.password_changed,
      }

threading.Thread(target=_accsepting ,args=(s, )).start()
threading.Thread(target=do_work,args=(obj,s)).start()
#cheak network
def cheak_net():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

#PopUP Notification namayesh midahad
def notification(messege):
    img =  os.path.abspath(os.getcwd()+'/Other/icon.png')
    subprocess.Popen(["notify-send", "-i", img, "PyChat", messege])
    playsound('Other/notify.mp3')
#sakhte image recapcha
#_________________________________________________________________________________________________UI_______________




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
        self.label_capcha= self.findChild(QLabel, "label")
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
        self.pushButton_3.setStyleSheet("background-color:transparent;border: 0px solid white;border-radius:20px;color:white;")
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
        self.Signin_BTN.setStyleSheet("background-color:  rgb(58, 175, 159);border: 1px solid rgb(58, 175, 159);border-radius:20px;color:white;")
        self.Signup1_BTN.setStyleSheet("background-color: transparent;border: 1px solid white;border-radius:20px;color:white;")
        self.Signin_BTN_2.setStyleSheet("background-color:  rgb(58, 175, 159);border: 1px solid rgb(58, 175, 159);border-radius:15px;color:white;")
        self.Signup1_BTN_7.setStyleSheet("background-color: transparent;border: 1px solid white;border-radius:20px;color:white;")
        self.Username_LE_3.setStyleSheet("background-color: transparent;border: 1px solid white;border-radius:20px;color:white;")
        self.Username_LE_16.setStyleSheet("background-color: transparent;border: 1px solid white;border-radius:20px;color:white;")
        self.Signin_BTN_4.setStyleSheet("background-color:  rgb(165, 165, 165);border: 1px solid rgb(58, 175, 159);border-radius:20px;color:white;")
        self.pushButton.setStyleSheet("background-color: transparent;border: 1px solid white;border-radius:20px;color:white;")
        self.Signin_BTN_3.setStyleSheet("background-color:  rgb(58, 175, 159);border: 1px solid rgb(58, 175, 159);border-radius:15px;color:white;")
        self.Signup1_BTN_2.setStyleSheet("background-color: transparent;border: 1px solid white;border-radius:20px;color:white;")
        self.Signin_BTN_5.setStyleSheet("background-color:  rgb(58, 175, 159);border: 1px solid rgb(58, 175, 159);border-radius:20px;color:white;")
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

            code=str(text)
        
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
                    image=response2.json()['picture']
                    self.Password_LE_4.setFocus()

                    ##############################

                    urllib.request.urlretrieve(image, '%s.jpg'%response2.json()['nickname'])
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
                cv2.rectangle(gray, (x+2, y+2), (x+2 + w, y+2 + h), (0, 0, 255), 4)
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
                cv2.rectangle(gray, (x+2, y+2), (x+2 + w, y+2 + h), (0, 0, 255), 4)
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
        wating_form(False,"")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def close_win(self):
        self.close()
    def capcha(self):
        img = ImageCaptcha()
        rnd_num=random.randint(10000, 100000)
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
        self.Signin_FRM.setGeometry(QtCore.QRect(22000, 0, 801, 541))  # dge nabayad to x=22000 ui bezaram chon mishe zir majmoaash
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

    def clickedBtn_login(self):#login page run mishe
        obj.user_want_sign_in(s)#dokme login aval
        wating_form(True,"signin")

    def clickedBtn_rigister(self):#OPEN RIGISTER PAGE
        obj.login(s,self.capcha_code)
        self.capcha()

class UI_Ads(QMainWindow):
    def __init__(self):
        super(UI_Ads, self).__init__()
        uic.loadUi("UI/Ads/Ads.ui", self)
        self.offset = None
        radius = 10.0
        path = QtGui.QPainterPath()
        img=QPixmap(os.path.abspath(os.getcwd() + '/UI/Ads/images/Ads.png'))
        self.ads_l.setPixmap(img)
        self.ads_l.setFixedWidth(img.width())
        self.ads_l.setFixedHeight(img.height())
        self.exit_b.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Ads/images/cross.png')))
        self.exit_b.setStyleSheet("background-color: transparent;border: 0px solid white;")
        self.exit_b.move(img.width()-32,10)
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





if (path.isfile('Other/lice_l_2.txt')):
    with open("Other/lice_l_2.txt") as file: # Use file to refer to the file object
        data = file.read()
        if data:
            print("login shodid!")
else:
    app = QApplication(sys.argv)
    window = UI_login()
    app.exec_()


