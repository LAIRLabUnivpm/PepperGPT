import os
#import subprocess
from openai import OpenAI
import time

client = OpenAI()
client.api_key = os.getenv('OPENAI_API_KEY')

def GPT_request(domanda):
    
    #tin = time.time()
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {"role": "system", "content": "You are a helpfull short assistant answering in only one sentence."},
        {"role": "user", "content": domanda},
    ]
    #max_tokens=20
    )
    
    #tout = time.time()

    answ = response.choices[0].message.content
    #print(f"GPT time: {tout-tin:.2f} sec")
    return answ


if __name__ == '__main__':
    while 1:
        question = str(input("Inserire domanda:   "))
        if question == 'stop': break
        risposta = GPT_request(question)
        print(risposta+"\n")
