import sounddevice as sd
from scipy.io.wavfile import write
import os
import winsound as bip
import time
#import audioToText as au

fs = 44100  # Sample rate
seconds = 5  # Duration of recording
fs_bip = 2000 #Hz
period_bip = 100 #ms

def soundRec():
    t0 = time.time()
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    print("Recording...")
    bip.Beep(fs_bip,period_bip*2)
    sd.wait()  # Wait until recording is finished
    bip.Beep(fs_bip,period_bip)
    bip.Beep(fs_bip,period_bip)
    print("...End")

    write('output.wav', fs, myrecording)  # Save as WAV file

    audiofile = "output1.wav"
    
    os.system("ffmpeg.exe -y -i output.wav "+audiofile)
    
    t1 = time.time()
    print("soundRec time: "+str(round(t1-t0-seconds,3))+ " sec")

    return audiofile


if __name__ == '__main__':
    audio = soundRec()
