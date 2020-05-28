import socket
import time
import os

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
size=s.recv(BUFFER_SIZE).decode()#file size
x=s.recv(BUFFER_SIZE).decode()#passvand file
down=0
recived_f = 'File_'+str(time.time()).split('.')[0]+"_"+str(x)
with open(recived_f, 'wb') as f:
    import sys
    while True:

        data = s.recv(BUFFER_SIZE)

        if not data:
            f.close()
            print('\nfile close()')
            break
        # write data to a file
        f.write(data)

        down = down + (sys.getsizeof(data)-33)
        percent=(100 * float(down)/float(size))
        print("\r",end="")
        print("{:.0f} %".format(percent),end="")



s.close()
