#to create data base for pychat users
import sqlite3
connection=sqlite3.connect("./users.db")
cur=connection.cursor()
sql="""
    CREATE TABLE IF NOT EXISTS  users(
    user_id VARCHAR (48),
    name VARCHAR(48),
    mail VARCHAR (60),
    pas VARCHAR (60) 
    
    );
    

"""
cur.execute(sql)
connection.commit()
connection.close()

