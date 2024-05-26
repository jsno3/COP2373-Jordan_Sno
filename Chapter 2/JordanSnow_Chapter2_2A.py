#
def spam():
    global cap_spam
    spam_list = ['100% free', 'Prize', 'Act now', 'Winner', 'Winning', 'You are a winner', 'Click here', 'Click below', 'Important information regarding', 'Congratulations', 'No catch', 'Not spam', 'Offer', 'Discount', 'Bargain', 'Amazing', 'Free', 'Deal', 'Click', 'Cheap', 'Earn', 'Cost', 'Best price', 'Credit', 'Cash', 'Apply', 'Gift', 'Debt', 'Receive', 'You have won']
    sorted_spam_list = sorted(spam_list)
    cap_spam = []
    for word in sorted_spam_list:
        cap_spam.append(word.title())


spam()


def main():
    global percent_spam
    spam_score = 0
    spam_words_detected = []

    message = input('Please enter the email/message you want scanned: ')
    if len(message) == 0:
        print('Please enter at least one word.')
        main()
    else:
        pass
    cap_message = message.title()
    message_length = len(message.split())
    for i in range(len(cap_spam)):
        if cap_spam[i] in cap_message:
            spam_words_detected.append(cap_spam[i])
            spam_score += 1

    percent_spam = round((spam_score / message_length) * 100)
    spam_likelihood = f'Out of the {message_length} words provided, {percent_spam}% of the words/phrases have been marked as common contents of spam emails.'

    print(f'\nYour provided email/message was: "{message}"\n')
    print(f'Your spam score for this email/message was: {spam_score}/{message_length}\n')
    if len(spam_words_detected) > 0:
        print('The following words/phrases within your email/message were detected as potential spam:')
        for word in spam_words_detected:
            print(f'"{word}"')
    else:
        print('No potential spam words/phrases detected.')

    print(f'\n{spam_likelihood}\n\nBased on this data, {sec()}\n')

    run = input('Would you like to enter another email/message? (y/n) ')
    if run == 'y':
        print('')
        main()
    elif run == 'Y':
        print('')
        main()
    else:
        print('\nThank you for using our spam detecting program.\nGoodbye!')
        exit()


def sec():
    if percent_spam <= 20:
        return "the provided email is very unlikely to be spam."
    elif percent_spam <= 40:
        return "the provided email is not likely to be spam."
    elif percent_spam <= 60:
        return "the provided email is probably spam."
    elif percent_spam <= 80:
        return "the provided email is likely to be spam."
    elif percent_spam <= 100:
        return "the provided email is very likely to be spam."


main()
