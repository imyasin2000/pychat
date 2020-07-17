import socket
import json
from queue import Queue 
import threading
import time
from select import select
import datetime
# import status
from tkinter import filedialog
from tkinter import *
import os
import sqlite3

q=Queue()
s=socket.socket()
s.connect(('192.168.109.1',14200))



f=''

class user :


    def __init__ (self):
        
        pass

    #ersal etelaat karbar jadid be samte server 
    def login(self,s:socket):
        self.data=[int(100)]
        self.username=input("enter your username :")
        self.data.append(self.username)
        self.name=input("enter your user name: ")
        self.data.append(self.name)
        self.email=input("enter your email :")
        self.data.append(self.email)
        self.password=input("enter your password :")
        to_chek_password=input("enter your password agian:")
        if self.cheking_password(self.password,to_chek_password):
            self.data.append(self.password)
            sending_to_server(s,self.data)

    #tabe baraye chek kardan motabegh budan password
    def cheking_password(self,pass1,pass2):
        if pass1==pass2:
            return True
        

        else:
            print("oh! try agian to enter password because ther r not equal try again ")
            self.password=input("enter your password :")
            to_chek_password=input("enter your password agian:")
            self.cheking_password(self.password,to_chek_password)


    def email_verify(self,s:socket,user_data:list):
        print(user_data[-1])
        if user_data[-1]==int(input("enter 8-digit code : ")):
            self.data1=[int(102)]+user_data[:-1]
            sending_to_server(s,self.data1)
            
        else:
            print("try angin ...")
            email_verify(self,s,user_data)


    #pasokh server be inke aya ba movafaghiat user jadid ra
    #be data base ezafe karde ya kheir
    def server_added_user_to_database(self,s:socket,data:list):
        print(data[0])


    def user_want_sign_in(self,s:socket):
        self.data=[int(103)]
        self.username=input("* enter your user name: *")
        self.data.append(self.username)
        self.password=input("enter your password: ")
        self.data.append(self.password)
        sending_to_server(s,self.data)



    def forgot_password(self,s:socket):
        self.eemail=input("enter your email: ")
        data=[int(101),'forgot','_',self.eemail]
        sending_to_server(s,data)

    def check_mail_forgotpass(self,s:socket,data:list):
        print(data[-1])
        code=int(input('open your email and enter 8-digit code :'))
        if int(data[-1])==code:
            pas=input('enter new password:')
            pas2=input('enter new passworda again :')
            self.cheking_password(pas,pas2)
            data1=[int(107),self.eemail,pas]
            sending_to_server(s,data1)
        else:
            print("codo barat print kardam dige chera eshtebah mizani?")

    def password_changed(self,s:socket,data:list):
        print(data[0])
        

    

    def send_text_message(self,s:socket,sender,reciver):
        message=input("enter text for sending to your friend : ")
        message_time=str(datetime.datetime.now())
        message_id=str(time.time())
        message_id=str(sender)+str(reciver)+message_id[:-3]
        data=[int(106),sender,reciver,message,message_time,message_id,'t']
        sending_to_server(s,data)

    def send_profilepic(self, s: socket,sender,reciver,usage):
        root = Tk()
        root.resizable(0, 0)
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=( ("all files", "*.*"),("jpeg files", "*.jpg"),("ppng files", "*.png")))
        name, ext = os.path.splitext(root.filename)
        x = os.path.getsize(root.filename) #size
        send_time=str(datetime.datetime.now())[:-4]
        media_id=str(sender)+str(reciver)+send_time
        media_id=media_id.replace(":","-")
        media_id=media_id.replace(' ','-')
        media_id=media_id.replace('.','-')
        root.destroy()
        down=0
        data = [int(108), sender,reciver,str(x),ext,b'start'.hex(),media_id,usage]  # pasvand file + size file
        sending_to_server(s, data)
        f = open(root.filename, 'rb')
        while True:
            l = f.read(20480)

            while (l):
                # f"{str(x)}{ext}{l}".encode()
                down = down + 20480
                percent = (100 * float(down) / float(x))-0.03
                print("{:.2f} %".format(percent),end="--")
                data = [int(108), sender,reciver,str(x),ext,l.hex(),media_id,usage,send_time]  # pasvand file + size file
                sending_to_server(s, data)
                l = f.read(20480)
            if not l:
                data = [int(108), sender,reciver,str(x),ext,b'end'.hex(),media_id,usage,send_time]
                sending_to_server(s, data)
                print("sended")
                break

    def profile_changed(self,s:socket,data:list):
        print('your profile changed :)')

    def add_friend(self,s:socket,token):
        friend=input("enter an id ...")
        data2=[int(121),token,friend]
        sending_to_server(s,data2)


    def failed_add_friend(self,socket,data):
        print('the username is not avaulable...')
    
    def friend_added(self,socket,data):
        print(f'{data[0]} , with name {data[1]} now is your friend his bio is {data[2]} and profile address is {data[3]}')
        connection = sqlite3.connect("./client.db")
        cur = connection.cursor()
        cur.execute(f"INSERT INTO friends VALUES (?,?,?,?)", (data[0], data[1], data[2], data[3]))
        connection.commit()
        connection.close()
        print('now your freind is ',chat_list(data[0]))
        return chat_list(data[0])





#--------------other func -------------------------------------------------

def recive_message(s:socket,data:list):
    number_of_message=len(data)
    print(f'\n{number_of_message} new message!')
    for mes in data:
        if mes[-1]=="t":
            print(f'{mes[0]} : {mes[2]} ({mes[3]})')
                # status.store_messages(i)
        elif mes[-1]=='v':
            print(f"voice message from {mes[0]} ---> address in our server is {mes[2]}")
            key=input("do you want to download this file?  enter Y or N ")
            if key=='Y':
                sending_to_server(s,[int(120),mes[2]])
            else:
                continue

        elif mes[-1]=='m':
            print(f"media from  {mes[0]} address in our server is {mes[2]}")
            key=input("do you want to download this file?  (enter Y or N )")
            if key=='Y':
                sending_to_server(s,[int(120),mes[2]])
            else:
                continue

        if str(mes[0])>str(mes[1]):
            tabale=str(mes[0]+str(mes[1]))
        else:
            tabale=str(mes[1]+str(mes[0]))
        connection = sqlite3.connect("./client.db")
        cursor = connection.cursor()

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

        cursor.execute(f"INSERT INTO {tabale} VALUES (?,?,?,?,?,?)", (mes[0], mes[1], mes[2], mes[3],mes[4],mes[5]))
        connection.commit()
    connection.close()
    
#---------------to adding new data in client database in each part  for loupe

def get_all_chat(your_name,your_friend):

        if str(your_name)>str(your_friend):
            tabale=str(your_name+str(your_friend))
        else:
            tabale=str(your_friend+str(your_name))

        connection=sqlite3.connect('./client.db')
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {tabale}")
        r = cursor.fetchall()
        connection.close()
        return r


def chat_list(friend=None):
    """the name of last ferind id optional"""
    connection = sqlite3.connect("./client.db")
    cursor = connection.cursor()


    if friend==NONE:
        cursor.execute("SELECT * FROM friends")
        r2 = cursor.fetchall()
        connection.close()
        return r2

    else:

        cursor.execute("SELECT * FROM friends WHERE user_id=?", (friend,))
        r = cursor.fetchall()
        if r==[]:
            cursor.execute("SELECT * FROM friends")
            r2 = cursor.fetchall()
            connection.close()
            return r2
        else:
            cursor.execute("DELETE FROM friends WHERE user_id=?", (friend,))
            connection.commit()
            cursor.execute(f"INSERT INTO friends VALUES (?,?,?,?)", (r[0][0], r[0][1], r[0][2], r[0][3]))
            connection.commit()
            cursor.execute("SELECT * FROM friends")
            r2 = cursor.fetchall()
            connection.close()
            return r2
















            




def receve_file(s:socket,data:list):
    global f
    recived_f =data[1]
    if bytes.fromhex(data[0])==b"start":
        f = open(recived_f, "wb")
    elif bytes.fromhex(data[0])==b"end":
        print(f"file from {data[0]} recived")
        f.close()
    else:
        f.write(bytes.fromhex(data[0]))
    

#----------------network connections with Queue--------------------------------

#in tabe tamame dade haye vorude be barname ra misanjad agar daraye etebar bashad 
#an hara accsept  mikonad 

def _accsepting(s:socket):
    data = b''
    while True:
        # try:

            #do taye dg niaz nabod
        r, _, _ = select([s], [s], [])#baresi mishe vasl hast ya na
        if r:
            d = s.recv(20480)
            data += d
            if len(d) < 20480:
                if data:
                    d = data.split(b'\0')
                    #extera baraye dycrypt ezafe beshe
                    #load_data(decrypt(d[i]))
                    for i in range(len(d) - 1):
                        load_data(d[i])
                        data = d[-1]
            else:
                pass
                    
        # except:
        #         print("connection failed ...")
        #         break
        #         # return



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
        if not q.empty():
            new_data=q.get()
            task=new_data[0]
            obj_work[f"{task}"](s,new_data[1:])
            #yasinmhd110@gmail.com
            q.task_done()




#--------------------------main--------------------------------------------------

obj=user()

obj_work={ 'token':"yasin78",
      '500':obj.email_verify,
      '502':obj.server_added_user_to_database,
      '509':obj.check_mail_forgotpass,
      '504':obj.password_changed,
      '503':recive_message,
      '509':obj.profile_changed,
      '510':receve_file,
      '511':obj.failed_add_friend,
      '512':obj.friend_added,

 
      }



threading.Thread(target=_accsepting ,args=(s, )).start()
threading.Thread(target=do_work,args=(obj,s)).start()

#in 2 khat baraye etesal avalie be server ast ta in ke server client mara be onvan 
#online zakhire konad #TODO #in tike ro bayad behtar konam 

token='user1'
im_online=[int(105),token]
sending_to_server(s,im_online)
# obj.send_profilepic(s,token,'yasin78','m')

# obj.add_friend(s,token)




# obj.login(s)
# obj.user_want_sign_in(s)
# obj.forgot_password(s)
for i in range(2):
    obj.send_text_message(s,token,token)

print(get_all_chat(token,token))
# obj.forgot_password(s)

# threading.Thread(target=obj.send_file,args=(s,token,'amin')).start()
# obj.send_voice_messege(s,'yasin78','yasin78')

