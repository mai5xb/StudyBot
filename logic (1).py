import os

def load_file(study):
    try:
        file_path = f"{study}.txt"
        with open(file_path, 'r') as f:
            lines = f.readlines()
            # reads each line in the file 'study'
            content = [line.strip() for line in lines if line.strip()]
        return content
    except FileNotFoundError:
        print(f"{study}not found")

def get_response(user_input, content):
    user_input = user_input.lower().strip()

    for i, line in enumerate(content):

        # Checks if the current line (the question) is a near match to the content in 'study'
        # We use 'in' to handle partial matches like "variable" matching "what is a variable?"
        if user_input in line.lower():

            # Found the question. The answer MUST be the next line (i + 1)
            if i + 1 < len(content):
                return content[i + 1]  # Answer is already stripped by load_file
            else:
                return ''

    # If the loop completes without a match
    return "Sorry, SodaBot doesn't have an answer for that :( \nTry typing 'faq' to see available questions."

def log_interaction(user_input, bot_response):
     with open('log.txt', 'a') as log:
        log.write(f"\nUser: {user_input}  \nSodaBot: {bot_response}")
