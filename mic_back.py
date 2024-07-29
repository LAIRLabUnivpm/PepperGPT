import speech_recognition as sr
import time
#import PepGPT as Pep

seconds = 5
fs = 16000

'''
class risposta:
    def risp(self):
        self.risp = ""
'''

def micCallback(rec, audioData):
    try:
        t0 = time.time()
        text = rec.recognize_google(audioData, language='it-IN', show_all=True)
        list_altern = text.get('alternative') #list -> [n]
        most_prob = list_altern[0] #dict
        testo_vero = most_prob.get('transcript') #string
        confid = most_prob.get('confidence')
        t1 = time.time()

        if testo_vero == 'stop':
            print("Exit...")
            exit()

        print("Text rec: "+testo_vero)   
        print(f"Confidence = {confid*100:.2f}%")
        print(f"Tempo convers: {t1-t0:.2f} sec")

        #risp = Pep.GPT_request(testo_vero+"\n")
        #print(risp)

    except sr.UnknownValueError:
        print("Audio non riconosciuto.\n")
        #return
    
    
def mic_background():
    
    r = sr.Recognizer()
    mic = sr.Microphone(sample_rate=fs)
    #r.energy_threshold = 3500
    
    print("\nRecording...")
    end_rec = r.listen_in_background(mic, phrase_time_limit=seconds, callback=micCallback)

    # stuff code with listening in background
    time.sleep(10) #while 1

    end_rec(wait_for_stop=True)
    print("...End")
    #exit()
    #time.sleep(5)

    # stuff code with no listening in background


def lista_mic():
    lista = sr.Microphone.list_microphone_names()
    indice = lista.index('Microfono (USBAudio1.0)')
    print("Indice: ",indice)
    #for mic in lista:
        #print(mic+'\n')


if __name__ == '__main__':
    #while 1:
        #mic_background()
    lista_mic()
    

