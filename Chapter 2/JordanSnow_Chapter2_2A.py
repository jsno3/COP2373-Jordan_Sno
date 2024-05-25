#
def spam():
    global cap_spam
    spam_list = ['100% free', 'Prize', 'Act now', 'Winner', 'Winning', 'You are a winner', 'Click here', 'Click below', 'Important information regarding', 'Congratulations', 'No catch', 'Notspam', 'Offer', 'Discount', 'Bargain', 'Amazing', 'Free', 'Deal', 'Click', 'Cheap', 'Earn', 'Cost', 'Best price', 'Credit', 'Cash', 'Apply', 'Gift', 'Debt', 'Receive', 'You have won']
    sorted_spam_list = sorted(spam_list)
    cap_spam = []
    for word in sorted_spam_list:
        cap_spam.append(word.title())
    print(sorted_spam_list)
    print(cap_spam)
    print(len(cap_spam))


spam()


def main():
    global spam_likelihood
    message_length = 0
    spam_score = 0
    spam_words_detected = []

    message = input('Please enter the email message you want scanned: ')
    cap_message = message.title()
    message_length = len(message.split())
    for i in range(len(cap_spam)):
        if cap_spam[i] in cap_message:
            print(cap_spam[i])
            spam_words_detected.append(cap_spam[i])
            spam_score += 1

    percent_spam = round((spam_score / message_length) * 100)
    spam_likelihood = (f'Out of the {message_length} words provided, {percent_spam}% of the words/phrases have been marked as common contents of spam emails.')



    print(spam_score)
    print(spam_words_detected)
    print(message)
    print(message_length)
    print(spam_likelihood)

main()

def sec():
    if spam_likelihood <= 20:
        return "The provided email is very unlikely to be spam."
    elif spam_likelihood <= 40:
        return "The provided email is not likely to be spam."
    elif spam_likelihood <= 60:
        return "The provided email is probably spam."
    elif spam_likelihood <= 80:
        return "The provided email is likely to be spam."
    elif spam_likelihood <= 100:
        return "The provided email is very likely to be spam."