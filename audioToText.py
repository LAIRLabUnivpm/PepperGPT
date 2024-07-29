import time
import speech_recognition as sr

def audioTotext(filename):
    t0 = time.time()

    #directory = "C:\\Users\\olegg\\Documents\\Registrazioni di suoni\\"
    #filename = directory + "test3.wav"

    #filename = "output1.wav"

    # initialize the recognizer
    r = sr.Recognizer()
    
    # open the file
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        #try:

        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data, language='it-IN', show_all=True) #dict -> get()
        list_altern = text.get('alternative') #list -> [n]
        most_prob = list_altern[0] #dict
        testo_vero = most_prob.get('transcript') #string
        confid = most_prob.get('confidence')
        #print(testo_vero)
        print("Confidence = " + str(round(confid*100,2)) + "%")

        tend = time.time()
        print("Tempo audioToText: " + str(round(tend-t0,3)) + " sec")

        return testo_vero
        #except:
            #print("Errore")

    

if __name__ == '__main__':
    text = audioTotext("C:\\Users\\olegg\\Desktop\\audiorecording.ogg")
    print(text)
