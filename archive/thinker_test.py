import os
from openai import OpenAI

if __name__ == "__main__":
    keyfile = open("locked.txt", "r")
    key = keyfile.read()
    #print(key)
    client = OpenAI(
        api_key=key
    )
    
    traits_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "What information can be gleaned about the author of the following Tweet?\
                    Please respond with any attributes/actions/experiences of the author as a bulleted list where each\
                    statement you make about the author starts with a '-'. Try to come up with at least 3: \
                    'Oh no that's cool.....sure pain! Come on in!! I was ONLY about to sleep!!'",
            }
        ],
        model="gpt-3.5-turbo-0125",
    )

    literal_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Reading following Tweet STRICTLY literally (as opposed to figuratively or sarcastically if you suspect there is such language in this Tweet), \
                summarize or rephrase this Tweet with the literal meaning. Do not mention any information about the intent of the author, only express the Tweet's literal meaning:\
                'Oh no that's cool.....sure pain! Come on in!! I was ONLY about to sleep!!'",
            }
        ],
        model="gpt-4o",
    )

    traits_content = traits_completion.choices[0].message.content
    literal_contents = literal_completion.choices[0].message.content

    #doing verdict prompt
    verdict_prompt = "We are attempting to determine if a Tweet is sarcastic, figurative (not sarcastic, but not literal), or neither (regular) without seeing the actual Tweet. \
    Based on the Tweet, we know the following about the author:\n" + traits_content + "\n"
    
    verdict_prompt += "This is the LITERAL meaning of the Tweet, read as though it had no sarcasm or figurative language (even if there is):" + literal_contents + "\n"
    verdict_prompt += "Please express your verdict with a single all lowercase word: either 'sarcasm', 'figurative', or 'regular'. Look for partial contradiction between traits and literal meaning for figurative language and total contradiction for sarcasm."
    
    verdict_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": verdict_prompt
            }
        ],
        model="gpt-4o",
    )

    verdict_content = verdict_completion.choices[0].message.content

    print(verdict_prompt)



    for thing in traits_completion:
        print(thing)
        print("\n")
    for thing in literal_completion:
        print(thing)
        print("\n")
    
    

    print(traits_content)
    print(literal_contents)
    print("VERDICT PROMPT:")
    print(verdict_prompt)
    print(verdict_content)
