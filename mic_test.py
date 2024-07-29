import speech_recognition as sr
import time
import PepGPT as Pep
import winsound as bip

seconds = 12
fs = 16000
fs_bip = 2000 #Hz
period_bip = 50 #ms

lista = sr.Microphone.list_microphone_names()
#indice = lista.index('Microfono (USBAudio1.0)')

def audioMic():
    r = sr.Recognizer()
    #r.energy_threshold = 100

    with sr.Microphone(sample_rate=fs,device_index=0) as source: #
        try: 
            print("\nRecording...")
            bip.Beep(fs_bip,period_bip)
            bip.Beep(fs_bip,period_bip)
            audio_data = r.listen(source, phrase_time_limit=seconds)#, timeout=20)
            bip.Beep(fs_bip,period_bip)
            bip.Beep(fs_bip,period_bip)
            print("...End")

            text = r.recognize_google(audio_data, language='it-IN', show_all=True) #dict -> get()
            list_altern = text.get('alternative') #list -> [n]
            most_prob = list_altern[0] #dict
            testo_vero = most_prob.get('transcript') #string
            confid = most_prob.get('confidence')

            print("Confidence = " + str(round(confid*100,2)) + "%")
            #print(f"Confidence = {confid*100:.2f}%")

            return testo_vero
        except sr.exceptions.UnknownValueError:
            return "Non ho capito, puoi ripetere?"

if __name__ == '__main__':
    testo = ''
    while 1:
        t0 = time.time()
        testo = audioMic()
        t2 = time.time()
        if testo == 'stop': break
        print("Text recorded: "+testo)
        print(f"Tempo tot: {t2-t0-seconds-(period_bip*3)/1000:.3f} sec\n")
        time.sleep(1)
        #risp = Pep.GPT_request(testo)
        #print("Risposta: " + risp)
    