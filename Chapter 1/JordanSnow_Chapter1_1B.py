# This program simulates a Magic 8 ball (a fortune telling toy that displays a random response to a yes or no question.)
# The responses of the Magic 8 ball will be written to a text file and then read later from that same text file and put into a list.
# After the responses are in a list they will be cleaned and converted into a dictionary to be assigned as values to a unique integer key (1-12).
# Finally, the program will display a question to the user, depending on their answer the program will randomly select one of the responses or quit.
# The program will not end unless closed externally or the user inputs: "goodbye"

# Define main
def main():

    # Main opens (or creates the file if it does not exist) named "8ball_responses.txt"
    f = open("8ball_responses.txt", "w")

    # A list named "responses" is created to easily layout the Magic 8 ball's phrases
    responses = ["Yes, of course!", "Without a doubt, yes.", "You can count on it.", "For sure!", "Ask me later!", "I'm not sure.", "I can't tell you right now.", "I'll tell you after my nap.", "No way!", "I don't think so.", "Without a doubt, no.", "The answer is clearly NO!"]

    # "responses" is then iterated through and written to the file: "8ball_responses.txt"
    for response in responses:
        f.write(f"{response}\n")

    # The file is closed
    f.close()


# Call main
main()


# Define secondary
def secondary():

    # Secondary opens and returns a list containing each line in the file: "8ball_responses.txt" as a list item and assigns it to the variable: "response_list"
    response_list = open("8ball_responses.txt").readlines()

    # Define a list named: "clean" to iterate through "response_list" and strip "\n" from each element
    clean = []

    # Set "clean_dictionary" to a global variable to be later used in "tertiary
    global clean_dictionary

    # Create an empty dictionary: "clean_dictionary" to match each response with an integer to be later randomly selected and displayed
    clean_dictionary = {}

    # Create an integer variable: "x" to be used as the keys for "clean_dictionary"
    x = 1

    # Iterate through each string in "response_list" and strip "\n" from each element. Append the resulting string to the list: "clean"
    for phrase in response_list:
        clean.append(phrase[0:-1])

    # Iterate through list: "clean" and assign each response to dictionary: "clean_dictionary" with a unique integer as their key
    for response in clean:
        clean_dictionary[x] = response
        x += 1


# Call secondary
secondary()


# Define tertiary
def tertiary():

    # Tertiary imports random to be later used to generate a random integer in a specified range
    import random

    # Define a variable: "y" that accepts input to either ask a yes/no question or say "goodbye" to end the program
    y = input("Please ask a question, enter 'goodbye' to stop. (yes/no) ")

    # If variable "y" is equivalent to "goodbye" print: "Thanks for playing! Goodbye!" and exit the program
    if y == 'goodbye':
        print("Thanks for playing! Goodbye!")
        exit()

    # Else, (variable "y" states anything other than "goodbye"):
    # 				Define variable "z" and assign it a random integer in the range of "clean_dictionary"
    # 				Print a "clean_dictionary" value based off of the generated key
    # 				Call tertiary.
    else:
        z = random.randrange(1, 13)
        print(clean_dictionary[z])
        tertiary()


# Call tertiary
tertiary()
