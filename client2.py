import pyaudio
import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import zlib





print("\nWelcome to Chat Room\n")
print("Initialising....\n")


s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = shost
name = "ali"
port = 6565
print("\nTrying to connect to ", host, "(", port, ")\n")

s.connect((host, port))
print("Connected...\n")
 
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

try:
    while True:
        data = s.recv(CHUNK)
        stream.write(data)
except KeyboardInterrupt:
    pass

print('Shutting down')
s.close()
stream.close()



