import socket
import json
from queue import Queue 
import threading
import time
from select import select
from PyQt5.QtWidgets import * #UI
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys
from os import path

q=Queue()
s=socket.socket()
s.connect(('0.0.0.0',1238))


code_g=0
class user :


    def __init__ (slef):

        pass

    #ersal etelaat karbar jadid be samte server 
    def login(self,s:socket,ui):
        self.data=[int(100)]
        self.username=ui.textedit_username.toPlainText()

        self.name=ui.textedit_fullname.toPlainText()

        self.email=ui.textedit_email.toPlainText()
        #cheak email is valid
        import re
        if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', self.email)):

            self.password = ui.textedit_password.toPlainText()
            to_chek_password = ui.textedit_repassword.toPlainText()
            if self.cheking_password(self.password, to_chek_password):
                self.data.append(self.username)
                self.data.append(self.name)
                self.data.append(self.email)
                self.data.append(self.password)
                sending_to_server(s, self.data)
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

        



    def code_enter_box(self):
        import tkinter as tk
        def show_entry_fields():
            global code_g
            code_g = e1.get()
            master.destroy()
        master = tk.Tk()
        tk.Label(master, text="Code ").grid(row=0)
        e1 = tk.Entry(master)
        e1.grid(row=0, column=1)
        tk.Button(master, text='Check', command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)
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


    #pasokh server be inke aya ba movafaghiat user jadid ra
    #be data base ezafe karde ya kheir
    def server_added_user_to_database(self,s:socket,data:list):
        print(data[0])


    def user_want_sign_in(self,s:socket,ui):
        self.data=[int(103)]
        self.username=ui.textedit_username.toPlainText()
        self.data.append(self.username)
        self.password=ui.textedit_password.toPlainText()
        self.data.append(self.password)
        sending_to_server(s,self.data)



    def forgot_password(self,s:socket):
        self.mail=input("enter your email: ")
        data=[int(102),_,_,self.email]
        sending_to_server(s,data)


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

            work[f"{task}"](s,new_data[1:])
            #yasinmhd110@gmail.com


            



            q.task_done()

obj=user()
work={'500':obj.email_verify,
      '502':obj.server_added_user_to_database,
      
      
      
      
      }


threading.Thread(target=_accsepting ,args=(s, )).start()
threading.Thread(target=do_work,args=(obj,s)).start()


#____________UI__________________________

class UI_login(QMainWindow):

    def __init__(self):
        super(UI_login, self).__init__()
        uic.loadUi("UI/Login_F.ui", self)
        self.button_login = self.findChild(QPushButton, "login_b")
        self.button_rigister = self.findChild(QPushButton, "rigister_b")
        self.button_forget = self.findChild(QPushButton, "forget_b")
        self.textedit_username = self.findChild(QTextEdit, "username_t")
        self.textedit_password = self.findChild(QTextEdit, "password_t")
        self.button_login.clicked.connect(self.clickedBtn_login)
        self.button_rigister.clicked.connect(self.clickedBtn_rigister)
        self.button_forget.clicked.connect(self.clickedBtn_forget)
        self.show()


    def clickedBtn_login(self):#login page run mishe

        obj.user_want_sign_in(s,self)

    def clickedBtn_rigister(self):#OPEN RIGISTER PAGE
        self.myOtherWindow = UI_rigister()
        self.myOtherWindow.show()
        self.hide()


    def clickedBtn_forget(self):#OPEN forget PAGE
        pass
        # obj.forgot_password(s)
        # self.myOtherWindow = UI_rigister()
        # self.myOtherWindow.show()
        # self.hide()

class UI_rigister(QMainWindow):
    def __init__(self):
        super(UI_rigister, self).__init__()
        uic.loadUi("UI/Rigister_F.ui", self)
        self.textedit_username = self.findChild(QTextEdit, "username_t")
        self.textedit_fullname = self.findChild(QTextEdit, "fullname_t")
        self.textedit_email = self.findChild(QTextEdit, "email_t")
        self.textedit_password = self.findChild(QTextEdit, "password_t")
        self.textedit_repassword = self.findChild(QTextEdit, "repassword_t")
        self.button_rigister = self.findChild(QPushButton, "rigister_b")
        self.button_rigister.clicked.connect(self.clickedBtn_rigister)


        self.show()


    def clickedBtn_rigister(self):#forget

        obj.login(s,self)

    def clickedBtn_2(self):#login
        pass




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


