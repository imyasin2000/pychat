from socket import socket
import threading  # run movazi
from extra import *
from datetime import datetime
import json
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import pyqrcode
import png
import random
from pyqrcode import QRCode
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

print("\nThe server was successfully activated.\n")

# Server information
## 51.195.19.3
ip = '51.195.53.142'
port = 1256


class Socket:
    size = 4096  # Size of information sent and received
    user_info = ""

    def __init__(self, host="192.168.1.107", port=14200):  # first run
        self.socket = socket()  # socket.socket()
        self.socket.bind((host, port))
        self.socket.listen(1)  # Open the port and wait for the new user
        while True:  # trade two function            #connect to client
            threading.Thread(target=self._wait_recv, args=self.socket.accept()).start()  # 2ta khorji conn,addr ghabli

    def _wait_recv(self, conn: socket, addr):  # waiting for new messege or conect or diconnect
        self._on_connect(conn)
        data = b''  # byte format
        while True:  # wait for new message
            try:
                d = conn.recv(self.size)
                data += d
                if len(d) < self.size:  # for biger bytes
                    if data:
                        d = data.split(b'\0')  # get meeseges \0 hi ali\0 hello\0
                        for i in range(len(d) - 1):
                            self._on_message(conn, decrypt(d[i]))  # client,messeg sended
                        data = d[-1]  # ali\0mohammad\0 bade \0 akhari ham mide msln bara kamel bodn payam
                    else:
                        conn.close()  # if client leave
            except:  # dissconect client
                self._on_disconnect(conn)
                return

    # addres karbar = client
    def _on_connect(self, client: socket):
        print(client, "start working with server")

    def _on_disconnect(self, client: socket):
        print(client, "disconnected")

    # dade haye daryafti ro bgir va client= yani ki in dade haro ferestade
    def _on_message(self, client: socket, data: bytes):
        x = (json.loads(data.decode()))
        task = x[0]
        work[f"{task}"](client, x[1:])

    # def send(client,ssdata):
    #     ssdata = json.dumps(ssdata)
    #     self.socket.send((ssdata.encode() + b'\0'))

    # client.send(#x["1"]())
    # close server
    def close(self):
        self.socket.close()


# vaghti ye nafar sabte nam mikone bayad motmaeen beshim
# ghablan inja account nadashe age dash behesh begim ghablan sabte nam kardi !
def login_chek(s: socket, data):
    user_id = data[0]
    sock = s
    connection = sqlite3.connect("./users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    r = cursor.fetchall()
    connection.close()
    if not r:
        print("login_chek")
        send_email(s, data)
        print("login_chek")
    else:
        print("exist")
        data1 = [int(502), " Username available! "]
        data1 = json.dumps(data1)
        s.send((data1.encode() + b'\0'))
        # sock.send(sock,"in data base ghablan vojud dashte")
        pass


# ersal mail baraye kasi ke faramush kade pass ash ra
# ya baraye user jadid
def send_email(s: socket, data: list):

    print(data)
    emialaddress = data[2]
    # setup the parameters of the message
    password = [97, 109, 105, 110, 109, 104, 102, 97]
    password = ''.join(chr(i) for i in password)
    msg = MIMEMultipart()
    msg['From'] = "PyChat Messenger"
    # message
    msg['To'] = emialaddress

    if data[0] == 'forgot':
        msg['Subject'] = "Forget password"
        
        random_number = (random.randint(100000, 1000000))
        message = (f"\nHi Dear {data[1]}.\n\n\n your code for change password is : {random_number} .")
        url = pyqrcode.create(str(random_number))
        url.png(os.getcwd() + '/Other/myqr.png', scale=10)
        img_data = open(os.getcwd() + '/Other/myqr.png', 'rb').read()
        image = MIMEImage(img_data, name=os.path.basename('myqr'))
        msg.attach(image)

        # add in the message body
    else:
        msg['Subject'] = "Subscription"
       
        random_number = (random.randint(100000, 1000000))
        message = (f"\nHi Dear {data[1]}.\n\n\n welcome to pychat! your verify code is : {random_number} .")
        url = pyqrcode.create(str(random_number))
        url.png(os.getcwd() + '/Other/myqr.png', scale=10)
        img_data = open(os.getcwd() + '/Other/myqr.png', 'rb').read()
        image = MIMEImage(img_data, name=os.path.basename('myqr'))
        msg.attach(image)

        # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    server.login("pychat.messenger@gmail.com", password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    data.append(random_number)
    if data[0] == 'forgot':
        data1 = [int(509)] + data  # email_verify
        data1 = json.dumps(data1)  # etelaat daryafti avalie + code random
        s.send((data1.encode() + b'\0'))
    else:
        # client_chek_mail(s,random_number)
        client_chek_mail(s, data)


# baad az ersal mail bayad be client khabr dade shavad ta
# mail khod ra chek konad

def client_chek_mail(s: socket, data):
    data = [int(500)] + data
    data = json.dumps(data)
    s.send((data.encode() + b'\0'))


def welcome_email(data: list):
    print(data)
    emialaddress = data[2]
    print(data[2])
    # setup the parameters of the message
    password = [97, 109, 105, 110, 109, 104, 102, 97]
    password = ''.join(chr(i) for i in password)
    msg = MIMEMultipart()
    msg['From'] = "PyChat Messenger"
    # message
    msg['To'] = emialaddress
    msg['Subject'] = "Welcome To PyChat"
    message = (f"\nHi Dear {data[1]}.\n\n\n welcome to pychat! Thanks for chosing PyChat.")
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    server.login("pychat.messenger@gmail.com", password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print(data)


def add_new_user(s: socket, data: list):
    # ghab in tabe tabe chek kardan username farakhani mishavad
    # agar chek kardan user name sahih bud in farakhani shavad
    connection = sqlite3.connect("./users.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO users VALUES (?,?,?,?)", (data[0], data[1], data[2], data[3]))
    connection.commit()
    connection.close()
    print(data)
    welcome_email(data)
    data1 = [int(502), "welcome to pychat !"]
    data1 = json.dumps(data1)
    s.send((data1.encode() + b'\0'))
    print("new_user_added")


def sign_in_request(s: socket, data: list):
    user_id = data[0]
    print(user_id)
    connection = sqlite3.connect("./users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    r = cursor.fetchall()
    connection.close()
    print(r)
    print(data[1])
    if r:
        if r[0][0] == data[0] and r[0][3] == data[1]:
            data1 = [int(502), "welcome to pychat!"]
            data1 = json.dumps(data1)
            s.send((data1.encode() + b'\0'))
        elif r[0][0] == data[0] and data[1] == 'd7c9dbcef6708effbdd973ebb0cbcef6708effbdd973eb':
            data1 = [int(502), "welcome to pychat!"]
            data1 = json.dumps(data1)
            s.send((data1.encode() + b'\0'))
        else:
            data1 = [int(502), "oh! usernme/password is not correct "]
            data1 = json.dumps(data1)
            s.send((data1.encode() + b'\0'))
    else:
        data1 = [int(502), "oh! usernme not found"]
        data1 = json.dumps(data1)
        s.send((data1.encode() + b'\0'))

    # erasl dastur be samte client va etela az hazf shodan az data base
    #


def edit_password(s: socket, data: list):
    print(data)
    connection = sqlite3.connect("./database.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET pas=? WHERE mail=?", (data[1], data[0]))
    connection.commit()
    connection.close()
    data1 = [int(504), "password changed !"]
    data1 = json.dumps(data1)
    s.send((data1.encode() + b'\0'))


# def send_ads()
work = {'100': login_chek, '101': send_email, '102': add_new_user, '103': sign_in_request,
        '107': edit_password}

s = Socket(ip, port)  # run socket init make object from socket

# s.send