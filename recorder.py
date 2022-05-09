import sounddevice as sound
from scipy.io.wavfile import write
import wavio as wav
import sys

try:
    freq = 44100            
    duration = 1800              #The duration of recording in seconds (It can be changed)
    #print("recording...")
    recording = sound.rec(int(duration*freq), samplerate=freq, channels=2)

    sound.wait()

except KeyboardInterrupt:          #Passes keyboard interrupts
    pass

write("recording.wav",freq,recording)       #Creates the .wav file


