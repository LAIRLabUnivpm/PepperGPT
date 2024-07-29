import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import datetime
import time
import PepGPT as Pep
#import audioToText as au
import mic_test as au
#import soundRec as sR
import GPT_assistant as assist

broker_IP = 'peppergpt'
#broker_IP = '172.24.146.200'
tin = 0
tout = 0
mode = 'assistant'

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/domanda1", qos=0) #QoS

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    tin = time.time()
    
    # escape sequence
    if msg.topic == '/domanda1' and msg.payload == b'stop':
       #publish.single("/risposta","stop",qos=2,hostname=broker_IP,protocol=mqtt.MQTTv31)
       print("\nExit external loop.")
       exit()

    # restart loop question
    if msg.topic == "/domanda1":
        print(msg.payload.decode('utf-8'))

    # register question on txt, call gpt and mqtt send response
    #audioname = sR.soundRec()
    #audioname = "output1.wav"
    #quest = au.audioTotext(audioname)
    quest = au.audioMic()
    #quest = input("Quesito: ")
    
    # escape sequence from audio
    if quest == "stop":
        publish.single("/risposta","stop",qos=2,hostname=broker_IP,protocol=mqtt.MQTTv31)
        print("\nExit internal loop.")
        return
    else:
        print("\nDomanda: "+ quest)
        with open("chat.txt","a+") as chat:
            t0 = datetime.datetime.now()
            chat.write(t0.strftime("%Y-%m-%d %H:%M:%S") + " Domanda: " + quest + "\n")

            if quest == 'Non ho capito, puoi ripetere?':
                risp = quest
            else:
                if mode == 'GPT': risp = Pep.GPT_request(quest)
                elif mode == 'assistant': risp = assist.GPT_Assistant(quest)
            
            t0 = datetime.datetime.now()
            chat.write(t0.strftime("%Y-%m-%d %H:%M:%S") + " Risposta: " + risp + "\n")

            publish.single("/risposta",risp,qos=2,hostname=broker_IP,protocol=mqtt.MQTTv31)#,client_id="Pepper")
            
            tout = time.time()
            print("Risposta: " + risp)
            print(f"Loop time: {tout - tin-5:2f} sec\n")


client = mqtt.Client(protocol=mqtt.MQTTv31,callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
    #client_id="ChatGPT"

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_IP, 1883, keepalive=180)

client.loop_forever()