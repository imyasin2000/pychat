import numpy as np
import cv2
import io
import socket
import struct
import time
import pickle
import zlib

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = shost
name = "ali"
port = 1238
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

cap = cv2.VideoCapture(0)


img_counter = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
while True:
    ret, frame = cap.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
#    data = zlib.compress(pickle.dumps(frame, 0))
    data = pickle.dumps(frame, 0)
    size = len(data)


    print("{}: {}".format(img_counter, size))
    s.sendall(struct.pack(">L", size) + data)
    img_counter += 1

    
cap.release()
cv2.destroyAllWindows()
