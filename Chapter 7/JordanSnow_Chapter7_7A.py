"""This program is intended to define a pattern using regular expressions that will
be used to separate and count any number of sentences that the user enters."""

# Import the Random Expression module to be used later in the program
import re


# Define main
def main():

    # Create a variable "pattern" and set it equal to a raw string that identifies
    # the start and the end of a sentence and takes everything in between the two
    pattern = r'(?:^|(?<=[?.!]\s))[A-Z\d].*?(?:\.{3}|[.!?])(?=(?: [A-Z\d])|$)'

    # Create a variable "entry" and set it equal to a string inputted by the user
    entry = input("Type in any number of sentences, including sentences which begin with numbers.")

    # Create a variable "number_of_sentences" and set it equal to the result of
    # referencing "entry" with "pattern" and use the flag "DOTALL" to capture sentences on more than one line
    number_of_sentences = re.findall(pattern, entry, flags=re.DOTALL)

    # Create a variable "length" that is set to the value of the length of "number_of_sentences"
    length = len(number_of_sentences)

    # For loop
    for sentence in number_of_sentences:

        # For "sentence" in "number_of_sentences" print(sentence
        print(sentence)

    # Print a formatted string that displays the number of sentences that the user entered
    print(f'There are {length} sentences.')


# Create dunder method to have "main" not run if my script is imported
if __name__ == '__main__':
    main()
