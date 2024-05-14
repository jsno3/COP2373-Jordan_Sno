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
    global buyers

    # Create if statement to sell tickets if there is any available
    if tickets <= 20:
        sold = input('How many tickets would you like to pre-purchase? (up to four can be purchased per customer) ')

        # Create if statement to check the amount of tickets the buyer is attempting to purchase
        if 0 < int(sold) <= 4 and int(sold) <= tickets:
            tickets -= int(sold)
            buyers += 1
            print('Thank you for your purchase!')
            print(f'There are {tickets} tickets remaining to be sold.\n')

        # Create an elif statement to catch too many tickets being accidentally purchased
        elif int(sold) > tickets:
            print(f'There are {tickets} ticket(s) available for sale.')
            print(f'Please enter an amount below or equal to {tickets}.\n')

        # Create an elif statement to catch negative number entries and entries over 4
        elif int(sold) <= 0 or int(sold) > 4:
            print(f'There are {tickets} ticket(s) available for sale.')
            print('Please enter an amount between 1 and 4 tickets.\n')
            main()

        # Create an if statement to check if the tickets are sold out, if they are end the program and print goodbye
        if tickets > 0:
            main()

        # Create an else statement to state the number of customers, say goodbye, and then exit the program
        else:
            print(f'{buyers} customers pre-purchased tickets.')
            print('Unfortunately, no more tickets are available for sale.')
            print('Goodbye!')
            exit()

# Call main
main()