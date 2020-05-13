from extra import *
import threading
import socket
import select


print("\nWelcome to Chat Room\n")
print("Initialising....\n")

shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = shost  # input(str("Enter server address: "))
port = 3235
print("\nTrying to connect to ", host, "(", port, ")\n")
print("Connected...\n")


class Socket:
    size = 4096

    def __init__(self, host, port):
        self.socket = socket.socket()
        self.socket.connect((host, port))
        threading.Thread(target=self._wait_recv).start()

    def _wait_recv(self):
        self._on_connect()
        data = b''
        while True:
            try:
                r, _, _ = select.select([self.socket], [self.socket], [])
                if r:
                    d = self.socket.recv(self.size)
                    data += d
                    if len(d) < self.size:
                        if data:
                            d = data.split(b'\0')

                            for i in range(len(d) - 1):
                                self._on_message(decrypt(d[i]))
                            data = d[-1]
                        else:
                            self.socket.close()
            except:
                self._on_disconnect()
                return

    def _on_connect(self):
        print(self.socket, 'joined.')

    def _on_disconnect(self):
        print(self.socket, 'disconnected.')

    def _on_message(self, data: bytes):
        print(self.socket, len(data.decode()))

    def close(self):
        self.socket.close()

    def send(self, data):
        self.socket.send(encrypt(data) + b'\0')


s = Socket(host, port)

while True:
    message = input("Enter a message: ")
    if message == "[e]":
        message = "Left chat room!"
        s.send(message.encode())
        print("\n")
        s.close()
        break

    s.send(message.encode())
