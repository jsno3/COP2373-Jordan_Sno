# This program is intended to pre-sell 20 tickets to prospective customers.
# Each customer can only purchase up to 4 tickets. The amount of tickets available will print out after each purchase.
# Finally, after all tickets are sold, the number of customers will be displayed and a goodbye message will print.


# Create Variables
tickets = 20
buyers = 0
sold = 0

# Define main
def main():

    # Make tickets and buyers global to avoid errors
    global tickets

    # Create if statement to sell tickets if there is any available
    if tickets <= 20:
        sold = input('How many tickets would you like to purchase? (up to four can be purchased per customer) ')

        # Create if statement to check the amount of tickets the buyer is attempting to purchase
        if 0 < int(sold) <= 4:
            tickets -= int(sold)
            print(f'There are {tickets} tickets remaining to be sold.')

        # Create an elif statement to catch negative number entries
        elif int(sold) <= 0:
            print('Please enter an amount between 1 and 4 tickets.')
            main()

        # Create an if statement to check if the tickets are sold out, if they are end the program and print goodbye
        if tickets > 0:
            main()
        else:
            print('No more tickets are available for sale, goodbye!')
            exit()

main()