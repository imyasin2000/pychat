import gtts
from playsound import playsound #++sudo apt-get install ffmpeg
import os
from pydub import AudioSegment
from pydub.playback import play


tts = gtts.gTTS('incoming call from'+ 'morteza seyed aghaee')
tts.save(os.getcwd()+'/incoming_call.mp3')
audio1 = AudioSegment.from_file(os.getcwd()+"/apple-orginal.mp3")
audio2 = AudioSegment.from_file(os.getcwd()+'/incoming_call.mp3')
mixed = audio1.overlay(audio2)  
play(audio2)
for i in range(0,2):#78 sec
    play(audio1)
    play(mixed) 
     
# os.remove(os.getcwd()+'/incoming_call.mp3') 
