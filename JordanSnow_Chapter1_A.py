# brief description of what the code is doing
tickets = 20
buyers = 0
sold = 0

def main():
    global tickets
    if tickets <= 20:
        sold = input('How many tickets would you like to purchase? (up to four can be purchased per customer) ')
        if  0 < int(sold) <= 4:
            tickets -= int(sold)
            print(f'There are {tickets} tickets remaining to be sold.')
        if tickets > 0:
            main()
        else:
            print('No more tickets are available, goodbye!')
            exit()

main()