from datetime import datetime, timedelta
from typing import List, Iterable
from numbers import Number
import json
import sqlite3


def encrypt(data: bytes) -> bytes:
    return data


def decrypt(data: bytes) -> bytes:
    return data

#not importent
def json_to_model(data: bytes, model):
    obj = model()
    obj.__dict__.update(json.loads(data.decode()))
    return obj

##'{"type":"login","user":"mhfa1380","pass":""}'

def make_object(v):#moteghayer to json readable
    if isinstance(v, (str, bool, Number)):
        return v

    if isinstance(v, Model):
        return v.dict()

    if isinstance(v, dict):
        return dict(map(lambda item: (item[0], make_object(item[1])), v.items()))

    if isinstance(v, Iterable):#list , map , ...
        return list(map(make_object, v))

    return str(v)


class Model:#base tamam model ha ke bdinim noeshon chie?
    def dict(self):
        return make_object(self.__dict__)

    def as_json(self):
        return json.dumps(self.dict()).encode()

    def __str__(self):
        return str(self.dict())


class Media(Model):
    id: str
    size: int

    def size_text(self):

        suffix = ('B', 'KB', 'MB', 'GB')
        size = self.size
        for i in range(len(suffix)):
            if size < 1024 or i == len(suffix) - 1:
                return '{:.1f} {}'.format(size, suffix[i])
            size /= 1024


class Voice(Media):
    pass


class Video(Media):
    pass


class Image(Media):
    pass


class File(Media):
    name: str


class User(Model):
    first_name: str
    last_name: str
    photos: List[Image]
    user_name: str

    def fullname(self):
        return self.first_name + ' ' + self.last_name


class Chat(Model):
    id: str
    photos: List[Image]

    def get_message(self, id):
        return Message()


class PrivateChat(Chat):
    user: User


class GroupChat(Chat):
    owner: User
    # admins: List[User]
    members: List[User]


class DateTime(datetime):

    def time_text(self):
        return self.time().strftime("%H:%M")

    def date_text(self):
        today = datetime.now().date()
        date = self.date()
        if today == date:
            return 'Today'
        elif today - timedelta(days=1) == date:
            return 'Yesterday'
        elif today.year == date.year:
            return date.strftime('%B %d')
        else:
            return date.strftime('%B %d, %Y')


class Message(Model):
    datetime: DateTime
    is_view: bool
    sender: User
    to: Chat
    reply_to: 'Message'


class TextMessage(Message):
    text: str


class WithTextMessage(TextMessage):
    has_text: bool


class VoiceMessage(WithTextMessage):
    voice: Voice


class VideoMessage(WithTextMessage):
    video: Video


class FileMessage(WithTextMessage):
    file: File


def adding_friends(data:list):
    '''
    clearly connection is our connection object to  user database that we 
    did it 
    r is a  cruded data(list) from database  and username is a person that 
    you want to add friend to him/her 
    '''
    user_that_send_response=data[0]
    connection = sqlite3.connect("./database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_that_send_response,))
    r = cursor.fetchall()
    if r==[]:
        return int(404)

    else:

        ls=json.loads(r[0][-1])
        if data[1] not in ls :
            ls.append(data[1])
            ls=json.dumps(ls)
            cursor.execute("UPDATE users SET freinds=? WHERE user_id=?", (ls,user_that_send_response))
            connection.commit()
            connection.close()

            connection = sqlite3.connect("./database.db")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE user_id=?", (data[1],))
            r2 = cursor.fetchall()
            data3=[int(512),r2[0][0],r2[0][1],r2[0][-2],r2[0][-3]]
            ls2=json.loads(r2[0][-1])
            if data[0] not in ls2:
                ls2.append(data[0])
                ls2=json.dumps(ls2)
                cursor = connection.cursor()
                cursor.execute("UPDATE users SET freinds=? WHERE user_id=?", (ls2,data[1]))
                connection.commit()
                connection.close()

            else:
                ls2.remove(data[0])
                ls2.append(data[0])
                ls2=json.dumps(ls2)
                cursor = connection.cursor()
                cursor.execute("UPDATE users SET freinds=? WHERE user_id=?", (ls2,data[1]))
                connection.commit()
                connection.close()
            print(data3)
            return data3
        else:
            ls.remove(data[1])
            ls.append(data[1])
            ls=json.dumps(ls)
            cursor = connection.cursor()
            cursor.execute("UPDATE users SET freinds=? WHERE user_id=?", (ls,user_that_send_response))
            connection.commit()
            connection = sqlite3.connect("./database.db")
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE user_id=?", (data[1],))
            r2 = cursor.fetchall()
            data3=[int(512),r2[0][0],r2[0][1],r2[0][-2],r2[0][-3]]
            ls2=json.loads(r2[0][-1])
            if data[0] not in ls2:
                ls2.append(data[0])
                ls2=json.dumps(ls2)
                cursor = connection.cursor()
                cursor.execute("UPDATE users SET freinds=? WHERE user_id=?", (ls2,data[1]))
                connection.commit()
                connection.close()

            else:
                ls2.remove(data[0])
                ls2.append(data[0])
                ls2=json.dumps(ls2)
                cursor = connection.cursor()
                cursor.execute("UPDATE users SET freinds=? WHERE user_id=?", (ls2,data[1]))
                connection.commit()
                connection.close()
            print(data3)
            return data3

        connection.close()












