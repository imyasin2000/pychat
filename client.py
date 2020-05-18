from extra import *
import threading
from socket import socket
from select import select #check is connected now or not
import json
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit
from PyQt5 import uic
import sys
<<<<<<< Updated upstream
=======
##
server = '192.168.1.107'#server address
port = 8871
>>>>>>> Stashed changes



server = '0.0.0.0'#server address
port = 8872

uname = ""#file as biron
toclient = ""

uname = input("youre name :  ")
toclient = input("youre freind name :  ")
class Socket:
    size = 4096

    def __init__(self, host, port,ui):
        self.socket = socket()
        self.socket.connect((host, port))#connected
        threading.Thread(target=self._wait_recv).start()#tabe movazi run mikne bara daryaft o send message
        #ready to add
        # self.UI=ui

    def _wait_recv(self):
        self._on_connect()
        data = b''
        while True:
            try:

                #do taye dg niaz nabod
                r, _, _ = select([self.socket], [self.socket], [])#baresi mishe vasl hast ya na
                if r:
                    d = self.socket.recv(self.size)
                    data += d
                    if len(d) < self.size:
                        if data:
                            d = data.split(b'\0')

                            for i in range(len(d) - 1):
                                self._on_message(decrypt(d[i]))
                            data = d[-1]
                        else:
                            self.socket.close()
            except:
                self._on_disconnect()
                return

    def _on_connect(self):

        user = ({"id": uname, "user": uname, "toclient": toclient})
        user = json.dumps(user)
        self.socket.sendall((user.encode()))#
        print(uname, 'joined.')

    def _on_disconnect(self):
        print(self.socket, 'disconnected.')

    def _on_message(self, data: bytes):
        x = (json.loads(data.decode()))
        print(x["from"], " : ", x["message"])
        ####add later
        # self.UI.messege((x["from"]," : ",x["message"]))


    def close(self):
        self.socket.close()

    def send(self, data):
        message_body = ({"username":uname,"message":data,"toclient":toclient})
        message_body=json.dumps(message_body)
        self.socket.send((message_body.encode()+ b'\0'))

        # self.socket.send(encrypt(data) + b'\0')#

#ready to add to clinet(do not open)
class UI(QMainWindow):


    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("Client_UI.ui", self)
        global server,port
        self.socket = Socket(server, port,self)
        self.textedit = self.findChild(QTextEdit, "textEdit")
        self.textedit_2 = self.findChild(QTextEdit, "textEdit_2")
        self.textedit_3 = self.findChild(QTextEdit, "textEdit_3")
        self.textedit_4 = self.findChild(QTextEdit, "textEdit_4")
        self.button = self.findChild(QPushButton, "pushButton")
        global uname
        self.textedit.setPlainText(uname)
        self.button.clicked.connect(self.clickedBtn)


        self.show()

    def messege(self,data):
        # self.textedit_4.setPlainText(str(data))
        print(data)

    def clickedBtn(self):
        global uname
        global toclient
        uname = (self.textEdit.toPlainText())
        toclient = (self.textedit_2.toPlainText())
        message = (self.textedit_3.toPlainText())
        self.socket.send(message)

#do not open
# app = QApplication(sys.argv)
# window = UI()
# app.exec_()

#######for yasin test#####
s = Socket(server, port,UI)
while True:
    message = input("")
    if message == "end":
        toclient = input("name dost jadid khod ra vare konid : ")
        message=""
    s.send(message)

