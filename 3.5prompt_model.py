from openai import OpenAI

if __name__ == "__main__":
    keyfile = open("locked.txt", "r")
    key = keyfile.read()
    print(key)
    client = OpenAI(
        api_key=key
    )
    
    file = open("tinySet.csv", "r")
    fileOut = open("test_prompt_output.csv","w")

    fileOut.write("EXPECTED,ACTUAL\n")

    Lines = file.readlines()
    
    for line in Lines:
        words = line.split(",")
        label = words[-1].strip()  # Remove newline character

        full_message = "Tell me if the following tweet is sarcasm, other figurative language, or neither (regular). "\
        "Please respond with a single all lowercase word, either 'sarcasm', 'figurative', or 'regular': \""

        full_message = full_message + words[0] + "\""
        
        print(full_message)

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": full_message,
                }
            ],
            model="gpt-3.5-turbo",
        )
    
        content = chat_completion.choices[0].message.content

        fileOut.write(label + "," + content + "\n")
        