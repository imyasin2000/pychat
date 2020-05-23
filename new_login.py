import socket
import json
from queue import Queue 
import threading
import time
from select import select

q=Queue()
s=socket.socket()
s.connect(('192.168.1.107',14200))


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
            return



#in tabe vorudi haue ghbel pardazesh ke az tabee marhale 
#ghabl amade ra decode mikonad va zemnan az halat json kharej 
#mikonad va an ha ra darun q put mikonad 
def load_data(data):
    x=(json.loads(data.decode()))
    q.put(x)

#ba farakhani in tabe har data ghbel fahm baraye server ra ersal 
#mikonim  in tabee khodkar tamame vorudi ash ra be json tablil karde
# va baad an ra ra encode mikond va ersal be server
def sending_to_server(socket:socket,data):
        data=json.dumps(data)
        socket.send((data.encode()+ b'\0'))

def create_worker():
    for i in range(7):
        print(q.get())
        q.task_done()
        
s.send("yes its work".encode())
threading.Thread(target=_accsepting ,args=(s, )).start()
create_worker()
print(q.empty())
s.close()

