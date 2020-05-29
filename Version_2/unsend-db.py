import sqlite3
import datetime
connection=sqlite3.connect("./unsend.db")
cur=connection.cursor()
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
connection.commit()
connection.close()

data=['amir','yasin78','bia bala:)',datetime.datetime.now(),'78782873a']
connection = sqlite3.connect("./unsend.db")
cur = connection.cursor()
cur.execute("INSERT INTO unsend VALUES (?,?,?,?,?)", (data[0], data[1], data[2], data[3],data[4]))
connection.commit()
connection.close()

