
from socket import socket
import threading #run movazi
from extra import *
from datetime import datetime
import json
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



print("\nThe server was successfully activated.\n")

#Server information

ip = '192.168.1.107'
port = 14200


class Socket:
    size = 4096 #Size of information sent and received
    user_info = ""

    def __init__(self, host="192.168.1.107", port=14200): #first run
        self.socket = socket() #socket.socket()
        self.socket.bind((host, port))
        self.socket.listen(1) #Open the port and wait for the new user

        while True:          # trade two function            #connect to client
            threading.Thread(target=self._wait_recv, args=self.socket.accept()).start() #2ta khorji conn,addr ghabli

    def _wait_recv(self, conn: socket, addr):#waiting for new messege or conect or diconnect
        self._on_connect(conn)
        data = b''#byte format
        while True:#wait for new message
            
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

    #addres karbar = client 
    def _on_connect(self, client: socket):
        print(client,"start working with server")


    def _on_disconnect(self, client: socket):
        print(client,"disconnected")


    #dade haye daryafti ro bgir va client= yani ki in dade haro ferestade
    def _on_message(self, client: socket, data: bytes):
        x=(json.loads(data.decode()))
        task=x[0]
        work[f"{task}"](client,x)
        y=x[1]
        y=json.dumps(y)
        client.send((y.encode()+b'\0'))
        print("data resived _onmassage")
        
    # def send(client,ssdata):
    #     ssdata = json.dumps(ssdata)
    #     self.socket.send((ssdata.encode() + b'\0'))


    #client.send(#x["1"]())
    #close server
    def close(self):
        self.socket.close()





#vaghti ye nafar sabte nam mikone bayad motmaeen beshim
#ghablan inja account nadashe age dash behesh begim ghablan sabte nam kardi ! 
def login_chek(s:socket,data):
    user_id=data[1]
    sock=s
    connection = sqlite3.connect("./users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    r = cursor.fetchall()
    connection.close()
    if r==[]:
        print("login_chek")
        send_email(s,data)
        print("login_chek")
    else:
        sock.send(sock,"in data base ghablan vojud dashte")


#ersal mail baraye kasi ke faramush kade pass ash ra 
#ya baraye user jadid
def send_email(s:socket,data):
    print(data)
    emialaddress=data[3]
    
# setup the parameters of the message
    password = [97, 109, 105, 110, 109, 104, 102, 97]
    password=''.join(chr(i) for i in password)
    msg = MIMEMultipart()
    msg['From'] = "messenger.verify.py@gmail.com"
    #message
    msg['To'] = emialaddress
    msg['Subject'] = "Subscription"
    import random
    random_number=(random.randint(100000,1000000))
    message = (f"\nHi Dear {emialaddress}.\n\n\n welcome to pychat! your verify code is : {random_number} .")
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    #client_chek_mail(s,random_number)
    client_chek_mail(s,random_number)

    
#baad az ersal mail bayad be client khabr dade shavad ta 
#mail khod ra chek konad 

def client_chek_mail(s:socket,random_n):
    data=[int(500),random_n]
    data = json.dumps(data)
    s.send((data.encode() + b'\0'))




def add_new_user(info: list):
    #ghab in tabe tabe chek kardan username farakhani mishavad 
    #agar chek kardan user name sahih bud in farakhani shavad 
    connection = sqlite3.connect("./users.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO users VALUES (?,?,?,?)", (info[1], info[2], info[3], info[4]))
    connection.commit()
    connection.close()



work={'100':login_chek , '101':send_email ,'500':add_new_user}
s=Socket(ip, port)#run socket init make object from socket
#s.send
