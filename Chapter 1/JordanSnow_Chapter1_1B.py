
def main():
    f = open("8ball_responses.txt", "w")
    responses = ["Yes, of course!", "Without a doubt, yes.", "You can count on it.", "For sure!", "Ask me later!", "I'm not sure.", "I can't tell you right now.", "I'll tell you after my nap.", "No way!", "I don't think so.", "Without a doubt, no.", "The answer is clearly NO!"]
    for response in responses:
        f.write(f"{response}\n")
    f.close()

main()

def secondary():
    list = open("8ball_responses.txt").readlines()
    clean = []
    global clean_dictionary
    clean_dictionary = {}
    x = 1
    for phrase in list:
        clean.append(phrase[0:-1])
    for response in clean:
        clean_dictionary[x] = response
        x += 1

secondary()

def tertiary():
    import random
    y = input("Please ask a question, enter 'goodbye' to stop. (yes/no) ")
    if y == 'goodbye':
        print("Thanks for playing! Goodbye!")
        exit()
    else:
        z = random.randrange(1, 13)
        print(clean_dictionary[z])
        tertiary()

tertiary()