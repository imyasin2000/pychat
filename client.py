from extra import *
import threading
from socket import socket
from select import select #check is connected now or not
import json

server = '51.195.19.3'#server address
port = 8876

uname = input("name khoda ra vare konid : ")
toclient = input("name dost khod ra vare konid : ")

# toclient = 'ali fadavi'
# uname = 'ahmad poor'
class Socket:
    size = 4096

    def __init__(self, host, port):
        self.socket = socket()
        self.socket.connect((host, port))#connected
        threading.Thread(target=self._wait_recv).start()#tabe movazi run mikne bara daryaft o send message

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
        print(x["from"]," : ",x["message"])

    def close(self):
        self.socket.close()

    def send(self, data):
        message_body = ({"username":uname,"message":data,"toclient":toclient})
        message_body=json.dumps(message_body)
        self.socket.send((message_body.encode()+ b'\0'))

        # self.socket.send(encrypt(data) + b'\0')#



s = Socket(server, port)

while True:

    message = input("")
    if message == "end":
        toclient = input("name dost jadid khod ra vare konid : ")
        message=""
    s.send(message)
