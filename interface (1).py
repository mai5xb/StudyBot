from logic import load_file, get_response, log_interaction
#allows us to use defined functions from another file


def main():
    print('Welcome to SodaBot!')
    user_name = input('What is your name? ').strip().title() #.title() capitalizes the first letter of the name
    print(f'Hello, {user_name}! SodaBot is here to give you a refreshing study experience!^_^')


    content = load_file("study")
    #assigns the contents of the file 'study' to the variable 'content'

    question_count = 0
    tip_count = 0
    challenge_count = 0
    #assigns 0 to important variables for summary analysis

    while True: #allows user to continue asking questions after being done with the first
        print("\nType: \n'faq' for Questions & Answers \n'tips' for SodaBot's Tips \\^o^/ \n'challenge' "
              "for some uniquely bubbly challenges (╹ڡ╹ ) \n'exit' to exit the program ( ﾟдﾟ)つ \nOr "
              "simply write your question!")
        print()
        user_input = input('What is your question?').strip().lower()
        #.lower() turns all the characters into lowercase (important since python is case-sensitive)


        if user_input == 'exit':
            print('Goodbye! SodaBot hopes to see you soon! ( ´･･)ﾉ(._.`)')
            break
        # when user types 'exit', program ends and exits loop

        elif user_input == 'faq':
            print("You can ask about:")
            inside_faq = False
            # this indicates that we are not yet in the FAQ section
            for line in content:
                if line.strip() == '[FAQ]':
                    inside_faq = True
                    continue
                elif line.strip().startswith("[") and inside_faq:
                    break
                elif inside_faq and line.strip():
                    print(f"-{line}")
                # prints the FAQ section
            # goes through each line in 'content' and searches for the FAQ section, if found assigns 'True' to the variable 'inside_faq'

        elif user_input == 'tips':
            tip_count += 1
            inside_tips = False
            print(" SodaBot Study Tips:")
            for line in content:
                if line.strip() == '[Tips]':
                    inside_tips = True
                    continue
                elif line.strip().startswith("[") and inside_tips:
                    break
                elif inside_tips and line.strip():
                    print(f"-{line}")


        elif user_input == 'challenge':
            challenge_count += 1
            inside_challenge = False
            print(" SodaBot Challenges:")
            for line in content:
                if line.strip() == '[Challenge]':
                    inside_challenge = True
                    continue
                elif line.strip().startswith("[") and inside_challenge:
                    break
                elif inside_challenge and line.strip():
                    print(f"-{line}")



        else:
            #in the case user asks a question
            question_count += 1
            response = get_response(user_input, content)
            print(f"SodaBot: {response}")
            log_interaction(user_input, response)


    print()
    print(f"SodaBot Summary for {user_name}")
    print(f"Number of questions asked: {question_count}")
    print(f"Number of tips requested: {tip_count}")
    print(f"Number of challenges requested: {challenge_count}")



main()
# calls function
