import gtts
from playsound import playsound

tts = gtts.gTTS('incoming call from'+ 'mohammad hossein fadavi')
tts.save("hello.mp3")
playsound("hello.mp3")