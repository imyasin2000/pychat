import time
import pyaudio
import socket
import select
 
print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)
 
s = socket.socket()
host = socket.gethostname()
print(s)
port = 6565

s.bind((host, port))

name = "server"
audio = pyaudio.PyAudio()          
s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")





def callback(in_data, frame_count, time_info, status):
    for s in read_list[1:]:
        s.send(in_data)
    return (None, pyaudio.paContinue)


# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, stream_callback=callback)
# stream.start_stream()

read_list = [s]
print ("recording...")

try:
    while True:
        readable, writable, errored = select.select(read_list, [], [])
        for s in readable:
            if s is s:
                (clientsocket, address) = s.accept()
                read_list.append(clientsocket)
                print ("Connection from"), address
            else:
                data = s.recv(1024)
                if not data:
                    read_list.remove(s)
except KeyboardInterrupt:
    pass


print ("finished recording")

s.close()
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
        
    
    