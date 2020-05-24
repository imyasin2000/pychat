import socket
import json
from queue import Queue 
import threading
import time
from select import select

q=Queue()
s=socket.socket()
s.connect(('192.168.1.107',14200))



class user :


    def __init__ (slef):
        
        pass

    #ersal etelaat karbar jadid be samte server 
    def login(self,s:socket):
        self.data=[int(100)]
        self.name=input("enter your name :")
        self.data.append(self.name)
        self.username=input("enter your user name: ")
        self.data.append(self.username)
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

    def server_added_user_to_database(self,s:socket,data:list):
        print(data[0])







#in tabe tamame dade haye vorude be barname ra misanjad agar daraye etebar bashad 
#an hara accsept  mikonad 

def _accsepting(s:socket):
    data = b''
    while True:
        time.sleep(0.02)
        try:

            #do taye dg niaz nabod
            r, _, _ = select([s], [s], [])#baresi mishe vasl hast ya na
            if r:
                d = s.recv(4096)
                data += d
                if len(d) < 4096:
                    if data:
                        d = data.split(b'\0')
                        #extera baraye dycrypt ezafe beshe
                        #load_data(decrypt(d[i]))
                        for i in range(len(d) - 1):
                            load_data(d[i])
                            data = d[-1]
                else:
                    s.close()
        except:
                print("connection failed ...")
                # return



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
        time.sleep(0.03)
        if not q.empty():
            new_data=q.get()
            print(new_data)
            task=new_data[0]

            work[f"{task}"](s,new_data[1:])
            #yasinmhd110@gmail.com


            



            q.task_done()

obj=user()
work={'500':obj.email_verify,'502':obj.server_added_user_to_database}


threading.Thread(target=_accsepting ,args=(s, )).start()
threading.Thread(target=do_work,args=(obj,s)).start()


obj.login(s)


