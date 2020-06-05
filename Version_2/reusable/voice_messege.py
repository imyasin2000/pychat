import pyaudio
import wave

def record_voice(filename):
    # filename = "recorded.wav"
    #not importent
    chunk = 1024
    FORMAT = pyaudio.paInt16
    channels = 1
    sample_rate = 44100
    p = pyaudio.PyAudio()
    #time of record
    record_seconds = 5

    stream = p.open(format=FORMAT,channels=channels,rate=sample_rate,input=True,output=True,frames_per_buffer=chunk)
    frames = []
    print("Recording...")
    for i in range(int(44100 / chunk * record_seconds)):
        data = stream.read(chunk)#save byte in moteghayer
        data1 = [int(108), sender, recever,data]
        stream.write(data)
        frames.append(data)
        
    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    # save audio file
    wf = wave.open(filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(sample_rate)
    wf.writeframes(b"".join(frames))
    wf.close()


record_voice("recorded.wav")
# record_voice("recorded2.wav")