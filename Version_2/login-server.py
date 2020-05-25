# to add new user
import sqlite3
import socket
import pickle
import json


def add_new_user(pychatid, yourname, email, pasword):
    connection = sqlite3.connect("./users.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO users VALUES (?,?,?,?)", (pychatid, yourname, email, pasword))
    connection.commit()
    connection.close()

def delet_ac(pychatid):
    


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.109.1", 14200))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)

data = conn.recv(4096)
data_variable = pickle.loads(data)
conn.close()
if data_variable[0] == "add":
    add_new_user(data_variable[1], data_variable[2], data_variable[3], data_variable[4])
# Access the information by doing data_variable.process_id or data_variable.task_id etc..,
print('Data received from client')
