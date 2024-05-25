#
def spam():
    global cap_spam
    spam_list = ['100% free', 'Prize', 'Act now', 'Winner', 'Winning', 'You are a winner', 'Click here', 'Click below', 'Important information regarding', 'Congratulations', 'No catch', 'Notspam', 'Offer', 'Discount', 'Bargain', 'Amazing', 'Free', 'Deal', 'Click', 'Cheap', 'Earn', 'Cost', 'Best price', 'Credit', 'Cash', 'Apply', 'Billion', 'Debt', 'Bankruptcy', 'Immediate delivery']
    sorted_spam_list = sorted(spam_list)
    cap_spam = []
    for word in sorted_spam_list:
        cap_spam.append(word.title())
    print(sorted_spam_list)
    print(cap_spam)
    print(len(cap_spam))


spam()


def main():
    spam_score = 0

    message = input('Please enter the message you want scanned: ')
    for word in message:
        for spam in cap_spam:
            if spam in message:
                spam_score += 1
    print(spam_score)


main()

