import sqlite3
import datetime
connection=sqlite3.connect("./database.db")
cur=connection.cursor()
sql="""
    CREATE TABLE IF NOT EXISTS  sent(
    sender VARCHAR (48),
    reciver VARCHAR(48),
    message VARCHAR (600),
    message_time DATETIME (60),
    message_id VARCHAR (60)


    
    );
    

"""
cur.execute(sql)

sql="""
    CREATE TABLE IF NOT EXISTS  unsend(
    sender VARCHAR (48),
    reciver VARCHAR(48),
    message VARCHAR (600),
    message_time DATETIME (60),
    message_id VARCHAR (60)


    
    );
    

"""
cur.execute(sql)

sql2="""
    CREATE TABLE IF NOT EXISTS  users(
    user_id VARCHAR (48),
    name VARCHAR(48),
    mail VARCHAR (60),
    pas VARCHAR (60) 
    
    );
    

"""
cur.execute(sql2)

connection.commit()
connection.close()


#data=['yasin78','yasin78','yasinmhd110@gmail.com','yasin']
#connection = sqlite3.connect("./database.db")
#cur = connection.cursor()
#cur.execute("INSERT INTO users VALUES (?,?,?,?)", (data[0], #data[1], data[2], data[3]))
#connection.commit()
#connection.close()