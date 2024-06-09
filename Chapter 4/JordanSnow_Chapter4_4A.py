# This program is intended to create a list of 30 common words/phrases used in spam messages.
# The program will then accept an email/message from the user to be "scanned" searching the inputted text for occurrences of the common spam words/phrases in this list.
# After the program has detected the amount of spam word/phrases it will print multiple lines informing the user of their spam score, the word/phrases that were detected as spam, and the likelihood that the text was spam.

import time


def make_timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        ret_val = func(*args, **kwargs)
        t2 = time.time()
        print('Time elapsed was', t2 - t1)
        return ret_val
    return wrapper


@make_timer
def count_nums(n):
    for i in range(n):
        for j in range(1000):
            pass


@make_timer
def run_2a():
    spam()
    main()


# Create spam
def spam():

    # Make cap_spam a global variable for use in main
    global cap_spam

    # Create spam_list to house the 30 spam words/phrases
    spam_list = ['100% free', 'Prize', 'Act now', 'Winner', 'Winning', 'You are a winner', 'Click here', 'Click below', 'Important information regarding', 'Congratulations', 'No catch', 'Not spam', 'Offer', 'Discount', 'Bargain', 'Amazing', 'Free', 'Deal', 'Click', 'Cheap', 'Earn', 'Cost', 'Best price', 'Credit', 'Cash', 'Apply', 'Gift', 'Debt', 'Receive', 'You have won']

    # Create sorted_spam_list to alphabetically organize spam_list
    sorted_spam_list = sorted(spam_list)

    # Create an empty list named cap_spam
    cap_spam = []

    # For loop to capitalize every word in sorted_spam_list and assign it to cap_spam
    for word in sorted_spam_list:

        # "cap_spam" is appended to with each "word" being capitalized
        cap_spam.append(word.title())


# Create main
def main():

    # Make percent_spam a global variable for use in sec
    global percent_spam

    # Create a variable named spam_score and set it equal to zero for use as a counter later in main
    spam_score = 0

    # Create an empty list named spam_words_detected to be used to count and store all detected spam words/phrases
    spam_words_detected = []

    # Create a variable named "message" that will accept a string input from the user
    message = input('Please enter the email/message you want scanned: ')

    # If/else statement
    # If the length of "message" is equal to zero (the user did not enter anything)
    if len(message) == 0:

        # Print('Please enter at least one word.')
        print('Please enter at least one word.')

        # Call main
        main()

    # Else statement
    else:

        # Pass to continue the function call
        pass

    # Create a variable called "cap_message" and assign the value of "message" with each word capitalized
    cap_message = message.title()

    # Define a variable named "message_length" and assign the length of each word in "message"
    message_length = len(message.split())

    # For loop
    # For "i" in the range of the length of "cap_spam" (30)
    for i in range(len(cap_spam)):

        # If "cap_spam[i]" in "cap_message"
        if cap_spam[i] in cap_message:

            # Append "spam_words_detected" with the value of "cap_spam[i]"
            spam_words_detected.append(cap_spam[i])

            # Add + 1 to the total value of "spam_score"
            spam_score += 1

    # Define "percent_spam" as the result of the rounded value of "spam_score" / "message_length" * 100
    percent_spam = round((spam_score / message_length) * 100)

    # Define spam_likelihood as a formatted string to later be displayed
    spam_likelihood = f'Out of the {message_length} words provided, {percent_spam}% of the words/phrases have been marked as common contents of spam emails.'

    # Print the provided email/message that the user entered
    print(f'\nYour provided email/message was: "{message}"\n')

    # Print the "spam_score" of that email/message
    print(f'Your spam score for this email/message was: {spam_score}/{message_length}\n')

    # If/else statement
    # If the length of "spam_word_detected" is greater than zero
    if len(spam_words_detected) > 0:

        # Print('The following words/phrases within your email/message were detected as potential spam:')
        print('The following words/phrases within your email/message were detected as potential spam:')

        # For loop
        # For "word" in "spam_words_detected"
        for word in spam_words_detected:

            # Print(f'"{word}"')
            print(f'"{word}"')

    # Else (There is no spam words/phrases detected)
    else:

        # print('No potential spam words/phrases detected.')
        print('No potential spam words/phrases detected.')

    # Print the likelihood that the entered email/message was spam based off of the result of the if/elif statements in sec
    print(f'\n{spam_likelihood}\n\nBased on this data, {sec()}\n')

    # Define a variable called "run" that accepts an input of a string to later continue or end the program
    run = input('Would you like to enter another email/message? (y/n) ')

    # If/else statement
    # If "run" equals 'y'
    if run == 'y':

        # Print an empty string '' (for a new line)
        print('')

        # Call main
        main()

    # Elif run equals 'Y'
    elif run == 'Y':

        # Print an empty string '' (for a new line)
        print('')

        # Call main
        main()

    # Else, (The user entered anything other than 'y' or 'Y')
    else:

        # Print Goodbye message
        print('\nThank you for using our spam detecting program.\nGoodbye!')

        # Close the program
        return


# Create sec
def sec():

    # If/elif statement
    # If percent_spam <= 20
    if percent_spam <= 20:

        # Return likelihood message
        return "the provided email is very unlikely to be spam."

    # Elif percent_spam <= 40
    elif percent_spam <= 40:

        # Return likelihood message
        return "the provided email is not likely to be spam."

    # Elif percent_spam <= 60
    elif percent_spam <= 60:

        # Return likelihood message
        return "the provided email is probably spam."

    # Elif percent_spam <= 80
    elif percent_spam <= 80:

        # Return likelihood message
        return "the provided email is likely to be spam."

    # Elif percent_spam <= 100
    elif percent_spam <= 100:

        # Return likelihood message
        return "the provided email is very likely to be spam."


run_2a()
