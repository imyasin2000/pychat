from datetime import datetime, timedelta
from typing import List, Iterable
from numbers import Number
import json



def encrypt(data: bytes) -> bytes:
    return data


def decrypt(data: bytes) -> bytes:
    return data


def json_to_model(data: bytes, model):
    obj = model()
    obj.__dict__.update(json.loads(data.decode()))
    return obj


def make_object(v):
    if isinstance(v, (str, bool, Number)):
        return v

    if isinstance(v, Model):
        return v.dict()

    if isinstance(v, dict):
        return dict(map(lambda item: (item[0], make_object(item[1])), v.items()))

    if isinstance(v, Iterable):
        l = []
        for i in v:
            l.append(make_object(i))
        return l

    return str(v)


class Model:
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
    admins: List[User]
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
