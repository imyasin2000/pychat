import sqlite3
import datetime
connection=sqlite3.connect("./client.db")
cur=connection.cursor()

sql="""
    CREATE TABLE IF NOT EXISTS  info(
    user_id VARCHAR (48),
    name VARCHAR(48),
    mail VARCHAR (60),
    internal_password VARCHAR (60),
    login INTEGER,
    bio VARCHAR(60),
    profile VARCHAR(70)





    
    );
    

"""
cur.execute(sql)

sql="""
    CREATE TABLE IF NOT EXISTS  friends(
    user_id VARCHAR (48),
    name VARCHAR(48),
    bio VARCHAR(60),
    profile VARCHAR(70)

    );
    

"""
cur.execute(sql)


connection.commit()
connection.close()


# data=['unknown','unknown','unknown','unknown',0]
# connection = sqlite3.connect("./client.db")
# cur = connection.cursor()
# cur.execute("INSERT INTO info VALUES (?,?,?,?,?)", (data[0], data[1], data[2], data[3],data[4]))
# connection.commit()
# connection.close()
