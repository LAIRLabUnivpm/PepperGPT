import os
#import subprocess
from openai import OpenAI
import time

client = OpenAI()
client.api_key = os.getenv('OPENAI_API_KEY')


# creation of assistent with features and prompt
assistente = client.beta.assistants.create(
    name = "Pepper",
    model="gpt-3.5-turbo-1106",
    instructions="You are a helpfull short assistant answering in only one sentence."
    #instructions="You are an assistive robot helping elder people doing everyday tasks."
    #tools=[{"type": "code_interpreter"}]
)

# create conversation thread 
mythread = client.beta.threads.create()

def GPT_Assistant(domanda):

    '''
    assistente = client.beta.assistants.create(
        name = "math teacher",
        model="gpt-3.5-turbo-1106",
        instructions="You are a personal math tutor. Write and run code to answer math questions.",
        tools=[{"type": "code_interpreter"}]
    )
        #"You are a robot imitating human conversations."'''
        
    
    # message to send
    messaggio = client.beta.threads.messages.create(
        thread_id = mythread.id,
        role="user", content = domanda
    )

    #tin = time.time()

    # send and get response
    run = client.beta.threads.runs.create(
        thread_id=mythread.id,
        assistant_id=assistente.id,
    )

    # wait for response
    print("Waiting...")
    while run.status != 'completed':
        retrieve_run = client.beta.threads.runs.retrieve(run_id=run.id,thread_id=mythread.id)
        if retrieve_run.status == 'completed':
            print("Stato richiesta: ",retrieve_run.status)
            break
    
    # print results
    response = client.beta.threads.messages.list(mythread.id)
    risp_assist = response.data[0].content[0].text.value
    #dom_user = messaggio.content[0].text.value
    #print(f"USER: {dom_user}")
    #print(f"ASSISTANT: {risp_assist}")
    #tout = time.time()
    #print(f"Tempo Assistant run: {tout-tin:.2f} sec\n")
    return risp_assist

    #chat.write(f"USER: {dom_user}\n")
    #chat.write(f"ASSISTANT: {risp_assist}\n")



if __name__ == '__main__':
    while 1:
        question = str(input("\nInserire domanda:   "))
        if question == 'stop': break
        risposta = GPT_Assistant(question)
    #print("Risposta:\t" + risposta + "\n")
