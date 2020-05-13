import socket
import threading
from extra import encrypt, decrypt

print("\nWelcome to Chat Room\n")
print("Initialising....\n")

host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 3235
print(host, "(", ip, ")\n")



class Socket:
    size = 4096
    clients = []

    def __init__(self, host, port):
        self.socket = socket.socket()
        self.socket.bind((host, port))
        self.socket.listen(1)
        while True:
            threading.Thread(target=self._wait_recv, args=self.socket.accept()).start()

    def _wait_recv(self, conn: socket.socket, addr):
        self._on_connect(conn)
        data = b''
        while True:
            try:
                d = conn.recv(self.size)
                data += d
                if len(d) < self.size:
                    if data:
                        d = data.split(b'\0')
                        for i in range(len(d) - 1):
                            self._on_message(conn, decrypt(d[i]))
                            self.sendall(conn, decrypt(d[i]))
                        data = d[-1]
                    else:
                        conn.close()
            except:
                self._on_disconnect(conn)
                return

    def _on_connect(self, client: socket.socket):
        self.clients.append(client)
        print(client, 'joined.')

    def _on_disconnect(self, client: socket.socket):
        self.clients.remove(client)
        print(client, 'disconnected.')

    def _on_message(self, client: socket.socket, data: bytes):
        print((data.decode()))

    def send_to(self, client, data):
        if isinstance(client, socket.socket):
            client.send(encrypt(data) + b'\0')
        else:
            for c in client:
                self.send_to(c, data)

    def sendall(self, data):
        for client in self.clients:
            self.send_to(encrypt(data) + b'\0')

    def close(self):
        self.socket.close()


Socket('0.0.0.0', port)
