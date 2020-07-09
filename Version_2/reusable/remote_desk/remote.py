import alsaaudio

m = alsaaudio.Mixer()
m.setvolume(int(m.getvolume()[0])+10)
print(m.getvolume())

####################### volume

