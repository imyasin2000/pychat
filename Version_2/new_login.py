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


q=Queue()
s=socket.socket()

#Server information
## 51.195.19.3
s.connect(('0.0.0.0',1239))

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
                self.data.append(self.password)

                if self.capcha_label==str(capcha_code):

                    sending_to_server(s, self.data)

                    wating_form(True)

                else:
                    window.lineEdit.clear()
                    QMessageBox.about(window, "recapcha error", "capcha code is not true")
                    window.lineEdit.clear()
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
        wating_form(False)
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
            wating_form(True)
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
            window.Signup_FRM.setGeometry(QtCore.QRect(22000, 0, 801, 541))
            window.Signin_FRM.setGeometry(QtCore.QRect(0, 0, 801, 541))
            window.Recover_FRM_4.setGeometry(QtCore.QRect(22000, 0, 801, 541))
            window.Username_LE.clear()
            window.Password_LE.clear()
            window.Username_LE.setFocus()


        wating_form(False)
        notification(data[0])


    def user_want_sign_in(self,s:socket):
        global window
        self.data=[int(103)]
        self.username=window.lineEdit_username.text()
        self.data.append(self.username)
        self.password=window.lineEdit_password.text()
        self.data.append(self.password)
        sending_to_server(s,self.data)



    def forgot_password(self,s:socket):
        global window
        global email_changer
        self.eemail = window.lineEdit_forgetemail.text()
        if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', self.eemail)):
            email_changer = self.eemail
            data = [int(101), 'forgot', '_', self.eemail]
            sending_to_server(s, data)
            wating_form(True)
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
        wating_form(False)

        window.Username_LE_3.clear()
        window.Username_LE_3.setFocus()

    def change_pass(self):
        global window
        global email_changer
        pas = window.lineEdit_forget_pass.text()
        pas2 = window.lineEdit_forget_repass.text()
        if self.cheking_password(pas, pas2) and pas!='':

            data1 = [int(107), email_changer, pas]
            sending_to_server(s, data1)
            wating_form(True)
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
        wating_form(False)
        window.Recover_FRM_3.setGeometry(QtCore.QRect(4555000, 4000, 801, 541))
        window.Signin_FRM.setGeometry(QtCore.QRect(0, 0, 801, 541))
        window.Username_LE.clear()
        window.Password_LE.clear()
        window.Username_LE.setFocus()
        notification(str(data[0]))




#--------------other func -------------------------------------------------
def wating_form(wating_until):
    global window
    if(wating_until):
        window.label_18.setHidden(False)
        window.label_18.setStyleSheet('background-color:rgba(255, 255, 255, 0.5);')
        movie = QtGui.QMovie(os.getcwd() + '/UI/Login/images/loading2.gif')
        window.label_18.setMovie(movie)
        movie.start()

    else:
        time.sleep(1)
        window.label_18.setHidden(True)
def regex_chek_email():
    pass



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
                # return



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


#_____________________________________________________________________________________________UI__________________________

class UI_login(QMainWindow):

    def __init__(self):
        global obj
        self.capcha_code = 0
        super(UI_login, self).__init__()
        uic.loadUi("UI/Login/Login_F.ui", self)
        self.offset = None
        radius = 55.0
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
        self.label_2.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/UI/Login/images/sidebar.png')))
        self.label_9.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/UI/Login/images/sidebar.png')))
        self.label_21.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/UI/Login/images/sidebar.png')))
        self.label_22.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/UI/Login/images/sidebar.png')))
        self.label_25.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/UI/Login/images/sidebar.png')))
        self.label_26.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/UI/Login/images/sidebar.png')))

        self.Username_LE.setFocus()
        self.Signup1_BTN.clicked.connect(self.Go_to_signup)
        self.pushButton.clicked.connect(self.Back_from_signup_to_signin)
        self.Forgotpass_BTN_2.clicked.connect(self.Go_to_recovery)
        self.Signin_BTN_2.clicked.connect(self.Go_to_varify)

        self.pushButton_6.clicked.connect(self.Back_from_recoverpass_to_signin)
        self.pushButton_4.clicked.connect(self.Back_from_varify_to_recoverpass)
        self.pushButton_5.clicked.connect(self.Back_from_changepass_to_varify)
        self.pushButton_13.clicked.connect(self.Go_to_signup)

        self.Signin_BTN_5.clicked.connect(obj.change_pass)
        self.pushButton_5.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/back.png')))
        self.pushButton_4.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/back.png')))
        self.pushButton_13.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/back.png')))
        self.pushButton_6.setIcon(QIcon(os.path.abspath(os.getcwd() + '/UI/Login/images/back.png')))

        self.Signin_BTN.clicked.connect(self.clickedBtn_login)
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
        self.pushButton_7.setStyleSheet("background-color: transparent;border: 1px solid transparent;")
        self.pushButton_8.setStyleSheet("background-color: transparent;border: 1px solid transparent;")
        self.pushButton_9.setStyleSheet("background-color: transparent;border: 1px solid transparent;")
        self.pushButton_15.setStyleSheet("background-color: transparent;border: 1px solid transparent;")
        self.pushButton_16.setStyleSheet("background-color: transparent;border: 1px solid transparent;")
        self.pushButton_14.setStyleSheet("background-color: transparent;border: 1px solid transparent;")
        self.pushButton_7.clicked.connect(self.close_win)
        self.pushButton_8.clicked.connect(self.close_win)
        self.pushButton_9.clicked.connect(self.close_win)
        self.pushButton_15.clicked.connect(self.close_win)
        self.pushButton_16.clicked.connect(self.close_win)
        self.pushButton_14.clicked.connect(self.close_win)


        self.Signup1_BTN_2.clicked.connect(obj.check_mail_forgotpass)
        self.Signup1_BTN_7.clicked.connect(obj.email_verify)


        self.center()
        self.show()

    def close_win(self):
        self.close()
    def capcha(self):
        img = ImageCaptcha()
        rnd_num=random.randint(10000, 100000)
        image = img.generate_image(str(rnd_num))
        image.save("Other/random.jpeg")
        self.label_capcha.setPixmap(QPixmap(os.path.abspath(os.getcwd() + '/Other/random.jpeg')))
        self.capcha_code = rnd_num

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
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



    # def Go_to_changepass(self):
    #     ###############################################

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

    #
    def clickedBtn_login(self):#login page run mishe

        obj.user_want_sign_in(s)

        wating_form(True)
    #
    def clickedBtn_rigister(self):#OPEN RIGISTER PAGE
        obj.login(s,self.capcha_code)
        self.capcha()




if (path.isfile('Other/lice_l_2.txt')):
    with open("Other/lice_l_2.txt") as file: # Use file to refer to the file object
        data = file.read()
        if data:
            print("login shodid!")
else:
    app = QApplication(sys.argv)
    window = UI_login()
    app.exec_()

# obj.login(s,self)
#obj.user_want_sign_in(s)
#obj.forgot_password(s)


