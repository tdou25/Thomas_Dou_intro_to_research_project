

if __name__ == "__main__":
    verdict_prompt = "We are attempting to determine if a Tweet is sarcastic, figurative, or neither (regular) without seeing the actual Tweet. \
    Based on the Tweet, we know the following about the author:\n" + "traits_content" + "\n"
    
    verdict_prompt += "This is the LITERAL meaning of the Tweet, read as though it had no Sarcasm or Figurative language (even if there is):" + "literal_contents" + "\n"

    verdict_prompt += "Please express your verdict with a single all lowercase word: either 'sarcasm', 'figurative', or 'regular':"
    print(verdict_prompt)