
def main():
    f = open("8ball_responses.txt", "w")
    responses = ["Yes, of course!", "Without a doubt, yes.", "You can count on it.", "For sure!", "Ask me later!", "I'm not sure.", "I can't tell you right now.", "I'll tell you after my nap.", "No way!", "I don't think so.", "Without a doubt, no.", "The answer is clearly NO!"]
    for response in responses:
        f.write(f"{response}\n")
    f.close()

main()

def sec():
    list = open("8ball_responses.txt").readlines()
    for phrase in list:
        print(phrase)

sec()