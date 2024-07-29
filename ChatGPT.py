import os
#import subprocess
from openai import OpenAI
import time

client = OpenAI()
client.api_key = os.getenv('OPENAI')

domanda = ""

while 1:

    domanda = str(input("Inserire domanda ('stop' per fermare):\t"))
    #domanda = "What is the capital of Paraguay?"
    print("You:\n" + domanda)
    if domanda == 'stop':
        print("Exit...\n")
        exit()

    tin = time.time()
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {"role": "system", "content": "You are a helpfull short assistant answering in only one sentence."},
        {"role": "user", "content": domanda},
    ]
    #max_tokens=20
    )

    tout = time.time()

    print("ChatGPT:")
    print(response.choices[0].message.content)
    print("\nExec time:\t" + str(round(tout-tin,2)) + " sec\n\n")

