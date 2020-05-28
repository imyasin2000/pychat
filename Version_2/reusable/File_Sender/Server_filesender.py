import socket
from threading import Thread
from tkinter import filedialog
from tkinter import *
TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024


class ClientThread(Thread):

    def __init__(self, ip, port, sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock


    def run(self):

        import os
        root = Tk()
        root.filename = filedialog.askopenfilename(initialdir="/home/mhfa1380/Desktop/", title="Select file",filetypes=(("all files","*.*"),("jpeg files","*.jpg"),))
        name, ext = os.path.splitext(root.filename)
        x=os.path.getsize(root.filename)
        print(type(ext))
        self.sock.send(str(x).encode())
        self.sock.send(ext.encode())
        f = open(root.filename, 'rb')

        while True:
            l = f.read(BUFFER_SIZE)
            while (l):
                self.sock.send(l)
                l = f.read(BUFFER_SIZE)
            if not l:
                f.close()
                self.sock.close()
                root.destroy()
                break


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)

    (conn, (ip, port)) = tcpsock.accept()

    newthread = ClientThread(ip, port, conn)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()