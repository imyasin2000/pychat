from socket import socket
import threading #run movazi
from extra import *
import json
import datetime


print("\nWelcome to Chat Room\n")
print("Initialising....\n")

ip = '0.0.0.0'
port = 8873


class Socket:
    size = 4096#hame taghir mikone
    clients = {}#save clients
    user_info =""
    def __init__(self, host, port): #first run
        self.socket = socket() #socket.socket()
        self.socket.bind((host, port))
        self.socket.listen(1)#open port and wait
        while True:          # trade two function            #connect to client
            threading.Thread(target=self._wait_recv, args=self.socket.accept()).start() #2ta khorji conn,addr ghabli

    def _wait_recv(self, conn: socket, addr):#waiting for new messege or conect or diconnect
        self._on_connect(conn)
        data = b''#byte format
        while True:#wait for new message
            try:
                d = conn.recv(self.size)
                data += d
                if len(d) < self.size:#for biger bytes
                    if data:
                        d = data.split(b'\0')#get meeseges \0 hi ali\0 hello\0
                        for i in range(len(d) - 1):
                            self._on_message(conn, decrypt(d[i]))#client,messeg sended
                        data = d[-1]#ali\0mohammad\0 bade \0 akhari ham mide msln bara kamel bodn payam
                    else:
                        conn.close()#if client leave
            except:#dissconect client
                self._on_disconnect(conn)
                return

    def _on_connect(self, client: socket):

        self.user_info = json.loads(client.recv(self.size))
        self.clients.update({client:self.user_info["user"]})
        print(self.user_info["user"], ' joined.')


    def _on_disconnect(self, client: socket):
        if client in self.clients:
            del self.clients[client]
        #print(self.clients)
        print(client, 'disconnected.')

    def _on_message(self, client: socket, data: bytes):
        x=(json.loads(data.decode()))
        for toclient, username in self.clients.items():
            if username == x["toclient"]:
                self.send_to(toclient, x["message"],x["username"])
                print("messege from : ",x["username"]," sended.")
        pass

    def send_to(self, client, data, mfrom):#kolan karesh ersale
        if isinstance(client, socket):#client ye socket hast ya na :
            message_body = ({"from": mfrom, "message": data, "time": "123"})
            message_body = json.dumps(message_body)
            client.send((encrypt(message_body)).encode() + b'\0')

        else:
            for c in client:
                self.send_to(c, data)

    def sendall(self, data):#send message to all onlion users
        for client in self.clients:
            self.send_to(client, data)

    def close(self):#close server
        self.socket.close()


s=Socket(ip, port)#run socket init make object from socket
#s.send
