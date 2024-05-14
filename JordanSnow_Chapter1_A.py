# brief description of what the code is doing
tickets = 20
sold = 0


def main():
    if tickets <= 20:
        sold = input('How many tickets would you like to purchase? ')
        tickets -= int(sold)
        print(format('There are {tickets} tickets remaining to be sold.'))
        if tickets > 0:
            main()
        else:
            print('No more tickets are available, goodbye!')
            exit()

main()