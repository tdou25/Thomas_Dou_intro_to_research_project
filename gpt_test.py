import os
from openai import OpenAI

if __name__ == "__main__":
    keyfile = open("locked.txt", "r")
    key = keyfile.read()
    print(key)
    client = OpenAI(
        api_key=key
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Tell me if the following tweet is sarcasm, figurative language, or neither (regular).\
                    Please respond with a single all lowercase word: either 'sarcasm', 'figurative', or 'regular': \
                    'Oh no that's cool.....sure pain! Come on in!! I was ONLY about to sleep!!'",
            }
        ],
        model="gpt-4o",
    )

    for thing in chat_completion:
        print(thing)
        print("\n")
    
    content = chat_completion.choices[0].message.content

    print(content)
