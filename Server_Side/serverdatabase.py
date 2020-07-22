import sqlite3
import datetime
import json
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
    profile VARCHAR(70),
    freinds VARCHAR(300)
    
    );
    

"""
cur.execute(sql2)

connection.commit()
connection.close()


# ls=['0','1','2']
# js=json.dumps(ls)
# data=['user1','mh reza','yasinmhd110@gmail.com','yasin','unkown','unknown',js]
# connection = sqlite3.connect("./database.db")
# cur = connection.cursor()
# cur.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?)", (data[0],data[1], data[2], data[3],data[4],data[5],data[6]))
# connection.commit()
# connection.close()