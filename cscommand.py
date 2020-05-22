#in module baraye ersal data az taraf client sakhte shode

import threading
from socket import socket
from select import select  # check is connected now or not
import json
import sys


#socket samte client 
class Socket:

    """
    yek class baarye ersal va daryaft etelaat va felan baraye ersal file nist
    bayad class socket ro 
    send() baraye ersal
    recive khodkar suraT migirad

    """

    size = 4096
    #default host va port ro gozashtam , age khastim jaye dige connect 
    #beshim moghe farakhani avazesh konim
    def __init__(self, host="192.168.1.107", port=14200):
        self.socket = socket()
        self.socket.connect((host, port))  # connected
        threading.Thread(target=self._wait_recv).start() # tabe movazi run mikne bara daryaft o send message
        # ready to add
        # self.UI=ui

    def _wait_recv(self):
        # self._on_connect()
        #mavared daryafti be byte hastan 
        data = b''
        while True:
            try:

                #se ta khoruji dare r yani readable hastan una
                r, _, _ = select([self.socket], [self.socket], [])  # baresi mishe vasl hast ya na
                if r:
                    d = self.socket.recv(32)
                    data += d
                    if len(d) < self.size:
                        if data:
                            d = data.split(b'\0')

                            for i in range(len(d) - 1):
                                #ramz gozari beshan
                                self.recive_data(d[i])
                            data = d[-1]
                        else:
                            self.socket.close()
            except:
                self._on_disconnect()
                return
                
    # def _on_connect(self):

    #     user = ({"id": uname, "user": uname, "toclient": toclient})
    #     user = json.dumps(user)
    #     self.socket.sendall((user.encode()))  #
    #     print(uname, 'joined.')

    def _on_disconnect(self):
        print(self.socket, 'disconnected.')

    def recive_data(self, data: bytes):
        new_data=(json.loads(data.decode()))
        print(new_data)
        new_task=new_data[0]

         


    def close_socket(self):
        self.socket.close_socket()
    #csdata yani client send data 
    def send(self, csdata):
        csdata = json.dumps(csdata)
        self.socket.send((csdata.encode() + b'\0'))



class user :

    def __init__ (slef):
        pass

    #ersal etelaat karbar jadid be samte server 
    def login(self,s:Socket):
        data=[int(100)]
        self.name=input("enter your name :")
        data.append(self.name)
        self.username=input("enter your user name: ")
        data.append(self.name)
        self.email=input("enter your email :")
        data.append(self.name)
        self.password=input("enter your password :")
        to_chek_password=input("enter your password agian:")
        if self.cheking_password(self.password,to_chek_password):
            data.append(self.name)
            s.send(data)

    #tabe baraye chek kardan motabegh budan password
    def cheking_password(self,pass1,pass2):
        if pass1==pass2:
            return True
        

        else:
            print("oh! try agian to enter password because ther r not equal try again ")
            self.password=input("enter your password :")
            to_chek_password=input("enter your password agian:")
            self.cheking_password(self.password,to_chek_password)





s=Socket()
yasin=user()
yasin.login(s)






        