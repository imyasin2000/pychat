import sqlite3
import datetime
connection=sqlite3.connect("./database.db")
cur=connection.cursor()

sql3=f"""
    CREATE TABLE IF NOT EXISTS  unsend(
    sender VARCHAR (48),
    reciver VARCHAR(48),
    message VARCHAR (600),
    message_time DATETIME (60),
    message_id VARCHAR (60),
    message_type VARCHAR (3)


    
    );
    

"""
cur.execute(sql3)

sql2="""
    CREATE TABLE IF NOT EXISTS  users(
    user_id VARCHAR (48),
    name VARCHAR(48),
    mail VARCHAR (60),
    pas VARCHAR (60),
    bio VARCHAR(60),
    profile VARCHAR(70)
    
    );
    

"""
cur.execute(sql2)

connection.commit()
connection.close()


data=['yasin78','yasin78','yasinmhd110@gmail.com','yasin','unkown','unknown']
connection = sqlite3.connect("./database.db")
cur = connection.cursor()
cur.execute("INSERT INTO users VALUES (?,?,?,?,?,?)", (data[0],data[1], data[2], data[3],data[4],data[5]))
connection.commit()
connection.close()