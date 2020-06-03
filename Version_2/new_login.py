import socket
import subprocess
import json
from queue import Queue 
import threading
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


q=Queue()
s=socket.socket()

#Server information
## 51.195.19.3
s.connect(('0.0.0.0',1237))


code_g=0
class user :


    def __init__ (self):

        pass

    #ersal etelaat karbar jadid be samte server 
    def login(self,s:socket,ui,capcha_code):
        self.data=[int(100)]
        self.username=ui.lineEdit_user.text()
        self.name=ui.lineEdit_name.text()
        self.email=ui.lineEdit_email.text()
        #cheak email is valid
        import re
        if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', self.email)):

            self.password = ui.lineEdit_pass.text()
            self.capcha_label = ui.lineEdit_capcha.text()
            to_chek_password = ui.lineEdit_repass.text()
            if self.cheking_password(self.password, to_chek_password):
                self.data.append(self.username)
                self.data.append(self.name)
                self.data.append(self.email)
                self.data.append(self.password)

                if self.capcha_label==str(capcha_code):
                    sending_to_server(s, self.data)
                else:
                    QMessageBox.about(ui, "recapcha error", "capcha code is not true")



                print("done")
            else:
                QMessageBox.about(ui, "password error", "oh! try agian to enter password because they are not equal!")

        else:
            QMessageBox.about(ui, "Invalid Email","enter valid email")




    #tabe baraye chek kardan motabegh budan password
    def cheking_password(self,pass1,pass2):
        if pass1==pass2:
            return True
        else:
            return False

        


    #vorodi bara gereftan code
    def code_enter_box(self):
        import tkinter as tk
        def show_entry_fields():
            global code_g
            code_g = e1.get()
            master.destroy()

        master = tk.Tk()
        master.title("Email confirmation")
        master.resizable(False, False)
        master.configure(bg='white')
        tk.Label(master, text=" ", bg="white").grid(row=0)
        tk.Label(master, text="     Youre Code   ", font=('', 9), bg="white").grid(row=1)
        e1 = tk.Entry(master)
        e1.grid(row=1, column=1)

        tk.Label(master, text="   ", bg="white").grid(row=1, column=4)
        tk.Label(master, text="     ", bg="white").grid(row=1, column=2)
        tk.Button(master, text=' Check ', bg="white", font=('', 8), command=show_entry_fields).grid(row=1, column=3,
                                                                                                    sticky=tk.W, pady=0)
        tk.Label(master, text=" ", bg="white").grid(row=3)
        tk.mainloop()

    def email_verify(self,s:socket,user_data:list):
        global code_g
        print("email cheak")
        print(user_data[-1])
        self.code_enter_box()
        if  user_data[-1] == int(code_g):
            self.data1 = [int(102)] + user_data[:-1]
            sending_to_server(s, self.data1)

        else:
            print("try angin ...")
            self.email_verify(s,user_data)


    #baraye namayesh messegebox
    def meesege_box(self,msg):
        import tkinter as tk
        root = tk.Tk()
        root.resizable(False, False)
        root.title(" server message ")
        w = tk.Label(root, text="\n     "+str(msg)+"     \n", bg="white")
        w.pack()
        # root.eval('tk::PlaceWindow . center')
        root.mainloop()


        # pasokh server be inke aya ba movafaghiat user jadid ra
        # be data base ezafe karde ya kheir
    def server_added_user_to_database(self,s:socket,data:list):
        # self.meesege_box(data[0])
        notification(data[0])


    def user_want_sign_in(self,s:socket,ui):
        self.data=[int(103)]
        self.username=ui.lineEdit_username.text()
        self.data.append(self.username)
        self.password=ui.lineEdit_password.text()
        self.data.append(self.password)
        sending_to_server(s,self.data)



    def forgot_password(self,s:socket,ui):
        self.eemail = ui.lineEdit_forgetemail.text()
        data = [int(101), 'forgot', '_', self.eemail]
        sending_to_server(s, data)

    def check_mail_forgotpass(self,s:socket,data:list):
        global code_g
        print("email cheak")
        print(data[-1])
        self.code_enter_box()
        if data[-1] == int(code_g):
            pas = input('enter new password:')
            pas2 = input('enter new passworda again :')
            self.cheking_password(pas, pas2)
            data1 = [int(107), self.eemail, pas]
            sending_to_server(s, data1)

        else:
            print("try angin ...")
            self.check_mail_forgotpass(s, data)

    def password_changed(self,s:socket,data:list):
        print(data[0])
#--------------other func -------------------------------------------------

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
            #yasinmhd110@gmail.com






            q.task_done()

obj=user()
obj_work={ 'token':"yasin78",
      '500':obj.email_verify,
      '502':obj.server_added_user_to_database,
      '509':obj.check_mail_forgotpass,
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
        self.capcha_code = 0
        super(UI_login, self).__init__()
        uic.loadUi("UI/Login/Login_F.ui", self)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        # self.button_forget = self.findChild(QPushButton, "forgotpass_b")
        self.lineEdit_username = self.findChild(QLineEdit, "Username_LE")
        self.lineEdit_password = self.findChild(QLineEdit, "Password_LE")


        self.lineEdit_name = self.findChild(QLineEdit, "Password_LE_3")
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

        self.Signup1_BTN.clicked.connect(self.Go_to_signup)
        self.pushButton.clicked.connect(self.Back_from_signup_to_signin)
        self.Forgotpass_BTN_2.clicked.connect(self.Go_to_recovery)
        self.Signin_BTN_2.clicked.connect(self.Go_to_varify)
        self.Signup1_BTN_2.clicked.connect(self.Go_to_changepass)
        self.pushButton_6.clicked.connect(self.Back_from_recoverpass_to_signin)
        self.pushButton_4.clicked.connect(self.Back_from_varify_to_recoverpass)
        self.pushButton_5.clicked.connect(self.Back_from_changepass_to_varify)
        self.Signin_BTN.clicked.connect(self.clickedBtn_login)
        # self.Signin_BTN.setStyleSheet("background-color:  teal;border: 1px solid teal;border-radius:15px;")
        # self.Signup1_BTN.setStyleSheet("background-color: rgb(58, 175, 159);border: 1px solid teal;border-radius:15px;")
        self.Signin_BTN_3.clicked.connect(self.clickedBtn_rigister)
        self.pushButton_2.clicked.connect(self.capcha)
        # self.Forgotpass_BTN_2.clicked.connect(self.clickedBtn_forget)
        self.pushButton_7.setStyleSheet("background-color: transparent;border: 1px solid transparent;")
        self.pushButton_8.setStyleSheet("background-color: transparent;border: 1px solid transparent;")
        self.pushButton_9.setStyleSheet("background-color: transparent;border: 1px solid transparent;")
        self.pushButton_7.clicked.connect(self.close_win)
        self.pushButton_8.clicked.connect(self.close_win)
        self.pushButton_9.clicked.connect(self.close_win)

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

    def Go_to_signup(self):

        self.Signin_FRM.setGeometry(QtCore.QRect(22000, 0, 801, 541))  # dge nabayad to x=22000 ui bezaram chon mishe zir majmoaash
        self.Signup_FRM.setGeometry(QtCore.QRect(0, 0, 801, 541))

    def Back_from_signup_to_signin(self):
        self.Signup_FRM.setGeometry(QtCore.QRect(22000, 0, 801, 541))
        self.Signin_FRM.setGeometry(QtCore.QRect(0, 0, 801, 541))

    def Go_to_recovery(self):
        self.Signin_FRM.setGeometry(QtCore.QRect(-1000, 0, 801, 541))
        self.Recover_FRM.setGeometry(QtCore.QRect(0, 0, 801, 541))

    def Go_to_varify(self):
        obj.forgot_password(s, self)
        # self.Recover_FRM.setGeometry(QtCore.QRect(-3000, 0, 801, 541))
        # self.Recover_FRM_2.setGeometry(QtCore.QRect(0, 0, 801, 541))


    def Go_to_changepass(self):
        self.Recover_FRM_2.setGeometry(QtCore.QRect(-2000, 0, 801, 541))
        self.Recover_FRM_3.setGeometry(QtCore.QRect(0, 0, 801, 541))

    def Back_from_recoverpass_to_signin(self):
        self.Recover_FRM.setGeometry(QtCore.QRect(25000, 0, 801, 541))
        self.Signin_FRM.setGeometry(QtCore.QRect(0, 0, 801, 541))

    def Back_from_varify_to_recoverpass(self):
        self.Recover_FRM_2.setGeometry(QtCore.QRect(35000, 0, 801, 541))
        self.Recover_FRM.setGeometry(QtCore.QRect(0, 0, 801, 541))

    def Back_from_changepass_to_varify(self):
        self.Recover_FRM_3.setGeometry(QtCore.QRect(4555000, 4000, 801, 541))
        self.Recover_FRM_2.setGeometry(QtCore.QRect(0, 0, 801, 541))

    #
    def clickedBtn_login(self):#login page run mishe

        obj.user_want_sign_in(s,self)
    #
    def clickedBtn_rigister(self):#OPEN RIGISTER PAGE
        obj.login(s, self,self.capcha_code)
        self.capcha()

    def clickedBtn_forget(self):#OPEN forget PAGE
        obj.forgot_password(s,self)


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


