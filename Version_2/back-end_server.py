
from socket import socket
import threading #run movazi
from extra import *
from datetime import datetime
import json
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys


print("\nThe server was successfully activated.\n")

#Server information

ip = '0.0.0.0'
port = 1425
online_users={}
f=""
#-------------------------------connection-------------------------------------------------------
class Socket:
    size = 4096 #Size of information sent and received
    user_info = ""

    def __init__(self, host="192.168.109.1", port=14200): #first run
        self.socket = socket() #socket.socket()
        self.socket.bind((host, port))
        self.socket.listen(1) #Open the port and wait for the new user
        while True: 
            try:
                     # trade two function            #connect to client
                threading.Thread(target=self._wait_recv, args=self.socket.accept()).start() #2ta khorji conn,addr ghabli
            except:
                print(" one client disconected...")

    def _wait_recv(self, conn: socket, addr):#waiting for new messege or conect or diconnect
        global online_users
        data = b''#byte format
        while True:#wait for new message
            try:
                d = conn.recv(self.size)
                data += d
                if len(d) < self.size:#for biger bytes
                    if data:
                        d = data.split(b'\0')#get meeseges \0 hi ali\0 hello\0
                        for i in range(len(d) - 1):
                            self._recive_data(conn, decrypt(d[i]))#client,messeg sended
                        data = d[-1]#ali\0mohammad\0 bade \0 akhari ham mide msln bara kamel bodn payam
                    else:
                        conn.close()#if client leave
            except Exception as inst:
                print(inst)
                del online_users[conn]
                # print(online_users)
                # print("disconected")
                # return


    #addres karbar = client 
    def _on_connect(self, client: socket):

        print(client,"start working with server")


    def _on_disconnect(self, client: socket):
        print(client,"disconnected")


    #dade haye daryafti ro bgir va client= yani ki in dade haro ferestade dar haghighat hamun 
    #conn hast
    def _recive_data(self, client: socket, data: bytes):
        x=(json.loads(data.decode()))

        task=x[0]
        work[f"{task}"](client,x[1:])
        
    # def send(client,ssdata):
    #     ssdata = json.dumps(ssdata)
    #     self.socket.send((ssdata.encode() + b'\0'))


    #client.send(#x["1"]())
    #close server
    def close(self):
        self.socket.close()

#---------------END----------------connection---------------------------END----------------------------




#-------------------------------FUNCTIONS------------------------------------------------------------------
#vaghti ye nafar sabte nam mikone bayad motmaeen beshim
#ghablan inja account nadashe age dash behesh begim ghablan sabte nam kardi ! 
def login_chek(s:socket,data):
    user_id=data[0]  #id_user khune 0 dade ersali ast 
    sock=s
    #peyda kardan karbar dar db
    connection = sqlite3.connect("./database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    r = cursor.fetchall()
    connection.close()
    if r==[]:
        print("login_chek")
        send_email(s,data)
        print("login_chek")
    else:
        #sock.send(sock,"in data base ghablan vojud dashte")
        pass


#ersal mail baraye kasi ke faramush kade pass ash ra 
#ya baraye user jadid
def send_email(s:socket,data:list):
    print(data)
    emialaddress=data[2]
    
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
    data.append(random_number)
    if data[0]=='forgot':
        data1=[int(509)]+data #email_verify
        data1 = json.dumps(data1) #etelaat daryafti avalie + code random 
        s.send((data1.encode() + b'\0'))


    else:
    
        #client_chek_mail(s,random_number)
        client_chek_mail(s,data)

    
#baad az ersal mail bayad be client khabr dade shavad ta 
#mail khod ra chek konad 

def client_chek_mail(s:socket,data):
    data=[int(500)]+data #email_verify
    data = json.dumps(data) #etelaat daryafti avalie + code random 
    s.send((data.encode() + b'\0'))




def add_new_user(s:socket,data: list):
    #ghab in tabe tabe chek kardan username farakhani mishavad 
    #agar chek kardan user name sahih bud in farakhani shavad 
    connection = sqlite3.connect("./database.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO users VALUES (?,?,?,?)", (data[0], data[1], data[2], data[3]))
    connection.commit()
    connection.close()
    data1=[int(502),"welcome to pychat!"]
    data1 = json.dumps(data1)
    s.send((data1.encode() + b'\0'))
    print("new_user_added")


#darkhast karbar baraye sign in amsde ast
def sign_in_request(s:socket,data:list):
    user_id=data[0]
    print(user_id)
    
    connection = sqlite3.connect("./database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    r = cursor.fetchall()
    connection.close()
    print('one user want sign in we crud data from data base ... : ',r)
    print(data[1])
    if r[0][0]==data[0] and r[0][3]==data[1]:
        data1=[int(502),"welcome to pychat!"]
        data1 = json.dumps(data1)
        s.send((data1.encode() + b'\0'))

    else :
        data1=[int(502),"oh! usernme/password is not correct "]
        data1 = json.dumps(data1)
        s.send((data1.encode() + b'\0'))

def edit_password(s:socket,data:list):
    print(data)
    connection=sqlite3.connect("./database.db")
    cursor=connection.cursor()
    cursor.execute("UPDATE users SET pas=? WHERE mail=?", (data[1],data[0]))
    connection.commit()
    connection.close()
    data1=[int(504),"password changed "]
    data1 = json.dumps(data1)
    s.send((data1.encode() + b'\0'))
    



#ezafe kardan yek karbar jadid be afrad online va ferastan payam hayie
#ke dar zaman ofline budan shakhs digari baraye vey ersal karde
#in payam ha az data base sent unsend migardad va dar data base sent 
#zakire migardad

def adding_new_client_to_online(s:socket,data:list):
    global online_users
    #-------add to online------------------------------------------------------
  
    
    print(data[0]+' connected!')
    online=data[0]
    online_users.update({s:data[0]})
    print(online_users)
    # print(online_users)
    #start sending pm that recived when client was ofline

    connection = sqlite3.connect("./database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM unsend WHERE reciver=?", (online,))
    r = cursor.fetchall()
    cursor.execute("DELETE FROM unsend WHERE reciver=?", (online,))
    if r!=[]:
        data=[int(503)]+r
        print("start sending unsend pm to user")
        data = json.dumps(data)
        s.send((data.encode() + b'\0'))
        print("sending pm finished")
        for i in r :
            if str(i[0])>str(i[1]):
                tabale=str(i[0]+str(i[1]))
            else:
                tabale=str(i[1]+str(i[0]))

            sql=f"""
                CREATE TABLE IF NOT EXISTS {tabale}(
                sender VARCHAR (48),
                reciver VARCHAR(48),
                message VARCHAR (600),
                message_time DATETIME (60),
                message_id VARCHAR (60),
                message_type VARCHAR (3)
                );
            """
            cursor.execute(sql)
            connection.commit()

            cursor.execute(f"INSERT INTO {tabale} VALUES (?,?,?,?,?,?)", (i[0], i[1], i[2], i[3],i[4],i[5]))
            connection.commit()
        connection.close()
        print(f'messages from {r[0][0]} to {r[1][1]} stored in our database ')

    else:
        connection.commit()
        connection.close()

#ersal payam haye daryafti be fard online va dar gheir in surat zakhire an ha 
#dar data base unsend
#---> data= [sender,reciver,message,message_time,message_id,'t']
def sending_messages(s:socket,data:list):
    global online_users
    print(data)
    for key, value in online_users.items(): 
        if data[1] == value: 
            data1=[int(503),(data[0],data[1],data[2],data[3],data[4],data[5])]
            data1 = json.dumps(data1)
            key.send((data1.encode() + b'\0'))
            connection = sqlite3.connect("./database.db")
            cur = connection.cursor()

            if str(data[0])>str(data[1]):
                tabale=str(data[0]+str(data[1]))
            else:
                tabale=str(data[1]+str(data[0]))

            sql=f"""
                CREATE TABLE IF NOT EXISTS {tabale}(
                sender VARCHAR (48),
                reciver VARCHAR(48),
                message VARCHAR (600),
                message_time DATETIME (60),
                message_id VARCHAR (60),
                message_type VARCHAR (3)
                );
            """
            cur.execute(sql)
            cur.execute(f"INSERT INTO {tabale} VALUES (?,?,?,?,?,?)", (data[0], data[1], data[2], data[3],data[4],data[5]))
            connection.commit()
            connection.close()
        else:
            print(data)
            connection = sqlite3.connect("./database.db")
            cur = connection.cursor()
            cur.execute("INSERT INTO unsend VALUES (?,?,?,?,?,?)", (data[0], data[1], data[2], data[3],data[4],data[5]))
            connection.commit()
            connection.close()
            print("message added to data base")

#[sender(0),reciver(1),str(x)  (2),ext(3),bf"{usage}".hex()  (4),media_id (5),usage (6), time(7)]

def add_picprofile(s:socket,data:list):
    global online_users
    global f

    recived_f = data[5]+data[3]

    if bytes.fromhex(data[4]) == b"start":
        f = open(recived_f, "wb")


    elif bytes.fromhex(data[4]) ==b"end":
        print(f"file from {data[0]} recived")
        print(data[-1])

        f.close()

        if data[-2]=='p':
            connection=sqlite3.connect("./database.db")
            cursor=connection.cursor()
            cursor.execute("UPDATE users SET profile=? WHERE user_id=?", (recived_f,data[0]))
            connection.commit()
            connection.close()
            data1=[int(509)]
            data1 = json.dumps(data1)
            s.send((data1.encode() + b'\0'))
        
        else:
            for key, value in online_users.items(): 
                if data[1] == value: 
                    data1=[int(503),(data[0], data[1],recived_f, data[-1],data[5],data[-2])]
                    data1 = json.dumps(data1)
                    key.send((data1.encode() + b'\0'))
                    connection = sqlite3.connect("./database.db")
                    cur = connection.cursor()

                    if str(data[0])>str(data[1]):
                        tabale=str(data[0]+str(data[1]))
                    else:
                        tabale=str(data[1]+str(data[0]))

                    sql=f"""
                        CREATE TABLE IF NOT EXISTS {tabale}(
                        sender VARCHAR (48),
                        reciver VARCHAR(48),
                        message VARCHAR (600),
                        message_time DATETIME (60),
                        message_id VARCHAR (60),
                        message_type VARCHAR (3)
                        );
                    """
                    cur.execute(sql)
                    cur.execute(f"INSERT INTO {tabale} VALUES (?,?,?,?,?,?)", (data[0], data[1],recived_f, data[-1],data[5],data[-2]))
                    connection.commit()
                    connection.close()
                    print(f"we recived a file from {data[0]}  , server sent this file to {data[1]} ")
                else:
                    connection = sqlite3.connect("./database.db")
                    cur = connection.cursor()
                    cur.execute("INSERT INTO unsend VALUES (?,?,?,?,?,?)", (data[0], data[1],recived_f, data[-1],data[5],data[-2]))
                    connection.commit()
                    connection.close()
                    print(f"we recived a file from {data[0]} but reciver ({data[1]}) is not online we stored this message in our data base...")




    else:

        f.write(bytes.fromhex(data[4]))


def send_file_to_client(s:socket,data1:list):
        data = [int(510),b'start'.hex(),data1[0]]
        data = json.dumps(data)
        print(data1)
        print(type(data1))
        s.send((data.encode() + b'\0'))
        path=data1[0]
        print(path)
        f = open(path, 'rb')
        while True:
            l = f.read(1024)

            while (l):
                # f"{str(x)}{ext}{l}".encode()
                data = [int(510),l.hex(),data1[0]]  # pasvand file + size file
                data = json.dumps(data)
                s.send((data.encode() + b'\0'))
                l = f.read(1024)
            if not l:
                data = [int(510),b'end'.hex(),data1[0]]
                data = json.dumps(data)
                s.send((data.encode() + b'\0'))
                print("file sent to client...")
                break

def to_check_friend_adding(s:socket,data:list):
    res=adding_friends(data)
    if res==int(404):
        data=[int(511)]
        data = json.dumps(data)
        s.send((data.encode() + b'\0'))
    else:
        data=res
        data = json.dumps(data)
        s.send((data.encode() + b'\0'))



    





#-----------------------------------------END FUNC ------------------------------------------------------------





work={'100':login_chek,'101':send_email,'102':add_new_user,'103':sign_in_request,'105':adding_new_client_to_online,'106':sending_messages,
      '107':edit_password,'108':add_picprofile,'120':send_file_to_client,'121':to_check_friend_adding}

s=Socket(ip, port)#run socket init make object from socket

#s.send
