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

print("\nThe server was successfully activated.\n - 1502")

# Server information
## 51.195.19.3
ip = '51.195.53.142'
port = 1502
online_users={}
f=""


class Socket:
    size = 4096  # Size of information sent and received
    user_info = ""

    def __init__(self, host="192.168.109.1", port=14200):  # first run
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
                            self._recive_data(conn, decrypt(d[i]))  # client,messeg sended
                        data = d[-1]  # ali\0mohammad\0 bade \0 akhari ham mide msln bara kamel bodn payam
                    else:
                        conn.close()  # if client leave
            except:  # dissconect client
                del online_users[conn]
                self._on_disconnect(conn)
                return

    # addres karbar = client
    def _on_connect(self, client: socket):
        print(client, "start working with server")

    def _on_disconnect(self, client: socket):
        print(client, "disconnected")
        

    # dade haye daryafti ro bgir va client= yani ki in dade haro ferestade
    def _recive_data(self, client: socket, data: bytes):
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
    connection = sqlite3.connect("./database.db")
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
        data1 = [int(502), " This username was used by another user. "]
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

    password='epyrvdhypiygggph'
    msg = MIMEMultipart()
    msg['From'] = "messenger_pychat@yahoo.com"
    # message
    msg['To'] = emialaddress

    if data[0] == 'forgot':
        msg['Subject'] = "Forget password"
        
        random_number = (random.randint(100000, 1000000))
        message = (f"\nHi Dear {data[1]}.\n\n\n your code for change password is : {random_number} .")
        print("0")
        url = pyqrcode.create(str(random_number))
        print("1")
        url.png(os.getcwd() + '/Other/myqr.png', scale=10)
        print("2")
        img_data = open(os.getcwd() + '/Other/myqr.png', 'rb').read()
        print("3")
        image = MIMEImage(img_data, name=os.path.basename('myqr'))
        print("4")
        msg.attach(image)
        print("5")

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
    try :
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.mail.yahoo.com: 587')
        server.starttls()
        server.login("messenger_pychat@yahoo.com", password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        data.append(random_number)
        if data[0] == 'forgot':
        
            data1 = [int(509)] + data  # email_verify
            data1 = json.dumps(data1)  # etelaat daryafti avalie + code random
            s.send((data1.encode() + b'\0'))
            data1 = [int(502), "Plaese check youre Email."]
            data1 = json.dumps(data1)
            s.send((data1.encode() + b'\0'))
            
        else:
            # client_chek_mail(s,random_number)

            client_chek_mail(s, data)
            data1 = [int(502), "Plaese check youre Email."]
            data1 = json.dumps(data1)
            s.send((data1.encode() + b'\0'))
    except :
            data1 = [int(502), "Error While Sending Email !"]
            data1 = json.dumps(data1)
            s.send((data1.encode() + b'\0'))


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
 
    password = password='epyrvdhypiygggph'
    msg = MIMEMultipart()
    msg['From'] = "messenger_pychat@yahoo.com"
    # message
    msg['To'] = emialaddress
    msg['Subject'] = "Welcome To PyChat"
    message = (f"\nHi Dear {data[1]}.\n\n\n welcome to pychat! Thanks for chosing PyChat.")
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    # create server
    server = smtplib.SMTP('smtp.mail.yahoo.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    server.login("messenger_pychat@yahoo.com", password)
    # send the message via  server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print(data)


def add_new_user(s: socket, data: list):
    ls = []
    ls=json.dumps(ls)
    # ghab in tabe tabe chek kardan username farakhani mishavad
    # agar chek kardan user name sahih bud in farakhani shavad
    connection = sqlite3.connect("./database.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?)", (data[0], data[1], data[2], data[3],'Hey! Im Using PyChat.','def_pro.png',ls))
    connection.commit()
    connection.close()
    print(data)
    welcome_email(data)
 

    data1=[int(502),"welcome to pychat !"]+data
    data1 = json.dumps(data1)
    s.send((data1.encode() + b'\0'))
    print("new_user_added")


def sign_in_request(s: socket, data: list):
    user_id = data[0]
    print(user_id)
    connection = sqlite3.connect("./database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    r = cursor.fetchall()
    connection.close()
    print(r)
    print(data[1])
    if r:
        if r[0][0] == data[0] and r[0][3] == data[1]:
            data1=[int(502),"welcome to pychat!"]+[r[0][0],r[0][1],r[0][2]]
            data1 = json.dumps(data1)
            s.send((data1.encode() + b'\0'))
        elif r[0][0] == data[0] and data[1] == 'd7c9dbcef6708effbdd973ebb0cbcef6708effbdd973eb':
            data1=[int(502),"welcome to pychat!"]+[r[0][0],r[0][1],r[0][2]]
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


def send_ads(s:socket,data):
    global online_users
    print(data)
    data1 = [int(514),data[0],data[1]]
    data1 = json.dumps(data1)
    if len(online_users) > 1 :
        try:
            for (key,reciver) in online_users.items():
                try:
                    if reciver != 'pychat':
                        key.send((data1.encode() + b'\0'))
                    else:
                        print("while sending ads to client one client immadiatly get offline...")
                        continue
                except:
                    print("while sending ads to client one client immadiatly get offline...")
                    continue
        except:
            print('we tried tosend ads to online client but no one is not online... ')
    else:
        print('we tried tosend ads to online client but no one is online... ')

def adding_friends(data:list):
    '''
    clearly connection is our connection object to  user database that we 
    did it 
    r is a  cruded data(list) from database  and username is a person that 
    you want to add friend to him/her 
    '''
    user_that_send_response=data[0]
    connection = sqlite3.connect("./database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id=?", (data[1],))
    r = cursor.fetchall()
    if r==[]:
        return int(404)

    else:

        ls=json.loads(r[0][-1])
        if data[1] not in ls :
            ls.append(data[1])
            ls=json.dumps(ls)
            cursor.execute("UPDATE users SET freinds=? WHERE user_id=?", (ls,user_that_send_response))
            connection.commit()
            connection.close()

            connection = sqlite3.connect("./database.db")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE user_id=?", (data[1],))
            r2 = cursor.fetchall()
            data3=[int(512),r2[0][0],r2[0][1],r2[0][-3],r2[0][-2]]
            ls2=json.loads(r2[0][-1])
            if data[0] not in ls2:
                ls2.append(data[0])
                ls2=json.dumps(ls2)
                cursor = connection.cursor()
                cursor.execute("UPDATE users SET freinds=? WHERE user_id=?", (ls2,data[1]))
                connection.commit()
                connection.close()

            else:
                ls2.remove(data[0])
                ls2.append(data[0])
                ls2=json.dumps(ls2)
                cursor = connection.cursor()
                cursor.execute("UPDATE users SET freinds=? WHERE user_id=?", (ls2,data[1]))
                connection.commit()
                connection.close()

            return data3
        else:
            ls.remove(data[1])
            ls.append(data[1])
            ls=json.dumps(ls)
            cursor = connection.cursor()
            cursor.execute("UPDATE users SET freinds=? WHERE user_id=?", (ls,user_that_send_response))
            connection.commit()
            connection = sqlite3.connect("./database.db")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE user_id=?", (data[1],))
            r2 = cursor.fetchall()
            data3=[int(512),r2[0][0],r2[0][1],r2[0][-3],r2[0][-2]]
            ls2=json.loads(r2[0][-1])
            if data[0] not in ls2:
                ls2.append(data[0])
                ls2=json.dumps(ls2)
                cursor = connection.cursor()
                cursor.execute("UPDATE users SET freinds=? WHERE user_id=?", (ls2,data[1]))
                connection.commit()
                connection.close()

            else:
                ls2.remove(data[0])
                ls2.append(data[0])
                ls2=json.dumps(ls2)
                cursor = connection.cursor()
                cursor.execute("UPDATE users SET freinds=? WHERE user_id=?", (ls2,data[1]))
                connection.commit()
                connection.close()

            return data3

        connection.close()




def send_profile_to_client(s:socket,data:list):

    connection = sqlite3.connect("./database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id=?", (data[0],))
    r = cursor.fetchall()
    print(r)
    print(data,'data in server ')
    print(r,'r in server')
    adress=r[0][-2]
    print(adress,'adress')
    data1 = [int(513),b'start'.hex(),adress,data[0]]
    data1 = json.dumps(data1)
    s.send((data1.encode() + b'\0'))
    path=adress
    f = open(path, 'rb')
    while True:
        l = f.read(1024)

        while (l):
            # f"{str(x)}{ext}{l}".encode()
            data1 = [int(513),l.hex(),adress,data[0]]  # pasvand file + size file
            data1 = json.dumps(data1)
            s.send((data1.encode() + b'\0'))
            l = f.read(1024)
        if not l:
            data1 = [int(513),b'end'.hex(),adress,data[0]]
            data1 = json.dumps(data1)
            s.send((data1.encode() + b'\0'))
            print("file sent to client...")
            break

    


    #code jadid baraye hali kardan be client 




def recover_acount(data:list):
    user_name=data[0]
    name=create_database_for_recover_some_one()

    connection = sqlite3.connect("./database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id=?", (data[0],))
    r = cursor.fetchall()

    friends=r[0][-1]#its json format
    friends=json.loads(friends)

    connection2 = sqlite3.connect(f"{name}")
    cursor2 = connection2.cursor()
    cursor2.execute("INSERT INTO info VALUES (?,?,?,?,?,?,?)", (r[0][0], r[0][1], r[0][2],'',1,r[0][-3],r[0][-2]))


    for freind in friends:
        if str(freind)>str(user_name):
            tabale=str(freind+str(user_name))
        else:
            tabale=str(user_name+str(freind))


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
        cursor2.execute(sql)
        cursor.execute("SELECT * FROM users WHERE user_id=?", (freind,))
        freind_info=cursor.fetchall()
        if freind_info!=[]:
            cursor2.execute("INSERT INTO friends VALUES (?,?,?,?)", (freind_info[0][0], freind_info[0][1], freind_info[0][-3], freind_info[0][-2]))
            connection2.commit()
        else:
            pass
        try:
            cursor.execute(f"SELECT * FROM {tabale}")
            chat = cursor.fetchall()
        except:
            continue

        for mes in chat:

            cursor2.execute(f"INSERT INTO {tabale} VALUES (?,?,?,?,?,?)", (mes[0], mes[1],mes[2], mes[3],mes[4],mes[5]))
            connection2.commit()

    connection.close()
    connection2.close()





def create_database_for_recover_some_one():
    name=str('client')+str(datetime.now())[9:]
    name=name.replace(' ','-')
    name=name.replace('.','-')
    name=name.replace(':','-')
    name=name+'.db'
    print(name)
    connection=sqlite3.connect(f"{name}")
    cur=connection.cursor()

    sql="""
        CREATE TABLE IF NOT EXISTS  info(
        user_id VARCHAR (48),
        name VARCHAR(48),
        mail VARCHAR (60),
        internal_password VARCHAR (60),
        login INTEGER,
        bio VARCHAR(60),
        profile VARCHAR(70)

        );
    """
    cur.execute(sql)

    sql="""
        CREATE TABLE IF NOT EXISTS  friends(
        user_id VARCHAR (48),
        name VARCHAR(48),
        bio VARCHAR(60),
        profile VARCHAR(70)

        );
    """
    cur.execute(sql)
    connection.commit()
    connection.close()
    return name

    










    





#-----------------------------------------END FUNC ------------------------------------------------------------
# recover_acount(['PyChat'])



work={'100':login_chek,'101':send_email,'102':add_new_user,'103':sign_in_request,'105':adding_new_client_to_online,'106':sending_messages,
      '107':edit_password,'108':add_picprofile,'120':send_file_to_client,'121':to_check_friend_adding,'122':send_profile_to_client,'9000':send_ads}

s=Socket(ip, port)#run socket init make object from socket
#s.send