import socket
import pickle
import json


class user:
    name = "yasin"
    family = "w"


def to_ask_user():
    user_info = ["add"]
    user_info.append(input("enter your pychatid: "))
    user_info.append(input("enter your name: "))
    user_info.append(input("enter your email: "))
    user_info.append(input("enter your password: "))
    return user_info


# ---------------------


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.109.1", 14200))

# Create an instance of ProcessData() to send to server.
variable = to_ask_user()
# Pickle the object and send it to the server
data_string = pickle.dumps(variable)
s.send(data_string)
s.close()
print('Data Sent to Server')
