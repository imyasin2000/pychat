import socket
import json
from queue import Queue 
import threading
import time
from select import select
import datetime

q=Queue()
s=socket.socket()
s.connect(('192.168.1.107',14200))





class user :


    def __init__ (slef):
        
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
        self.mail=input("enter your email: ")
        data=[int(102),_,_,self.email]
        sending_to_server(s,data)
        pass


    def send_text_message(self,s:socket,sender,reciver):
        message=input("enter text for sending to your freind : ")
        message_time=datetime.datetime.now()
        message_id=str(time.time())
        message_id=message_id[:-3]+work['token']
        data=[int(104),sender,reciver,message,message_time,message_id]
        sending_to_server(s,data)
    
    




        



#--------------other func -------------------------------------------------

def regex_chek_email():
    pass

    

    


#----------------network connections with Queue--------------------------------

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
            task=new_data[0]

            work[f"{task}"](s,new_data[1:])
            #yasinmhd110@gmail.com

            q.task_done()



#--------------------------main--------------------------------------------------

obj=user()

work={ 'token':"yasin78",
      '500':obj.email_verify,
      '502':obj.server_added_user_to_database,
      
 
      }


threading.Thread(target=_accsepting ,args=(s, )).start()
threading.Thread(target=do_work,args=(obj,s)).start()

#in 2 khat baraye etesal avalie be server ast ta in ke server client mara be onvan 
#online zakhire konad #TODO #in tike ro bayad behtar konam 
try:
    token='yasin78'
    im_online=[int(105),token]
    sending_to_server(s,im_online)
    print("done")
except:
    print("chek your internet and try")

#obj.login(s)
#obj.user_want_sign_in(s)
#obj.forgot_password(s)


