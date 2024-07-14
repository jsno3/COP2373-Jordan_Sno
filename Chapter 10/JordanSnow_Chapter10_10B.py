""" The purpose of this program is to create a class named 'BankAcct' that can hold information
including name, account number, amount, and interest rate. Additionally, this class has methods to
adjust the interest rate, withdraw and deposit funds (has been replaced with 'add' and 'sub' methods from 'Money'
using inheritance), give the current balance, and predict interest based off of the user's current balance,
interest rate, and a specified time frame (in days). 'BankAcct' also has the ability to display the user's name,
account number, balance, and interest rate in a formatted matter. Finally, 'main' and 'test_func'
work in conjunction to test the class's functionality and methods.
"""


# Import Decimal from decimal
from decimal import Decimal


# Define class "Money" that inherits "Decimal"
class Money(Decimal):

    # Use __new__ to call the superclass version of __new__, pass in 'cls' to reference the class,
    # 'amount' to reference the amount of money (add in that the variable should be a Decimal), and "units='USD'"
    # to assign 'USD' to the money in said class
    def __new__(cls, name, account_number, amount: Decimal, interest_rate, units='USD'):

        # return the superclass version of __new__
        return super(Money, cls).__new__(cls, amount)

    # Initialize variables 'v' and 'units'
    def __init__(self, name, v: Decimal, units='USD'):

        # Assign 'self.name' to the variable 'name'
        self.name = name

        # Assign 'self.v' to the variable 'v'
        self.v = v

        # Assign 'self.units' to the variable 'units'
        self.units = units

    # Define __str__(self) to return a formatted string containing 'self.v' and 'self.units'
    def __str__(self):

        # Return the formatted string containing 'self.v' and 'self.units'
        return f'You have {self.v:.2f} {self.units}'

    # Define __add__ passing in 'self' and 'value'
    def __add__(self, value):

        # Add variables 'self.v' and 'value' and set 'self.v' equal to the result
        self.v += value

        # Return the value of 'self'
        return self

    # Define __sub__ passing in 'self' and 'value'
    def __sub__(self, value):

        # Subtract variables 'self.v' and 'value' and set 'self.v' equal to the result
        self.v -= value

        # Return the value of 'self'
        return self


# Define class 'BankAcct' passing in 'Money' for inheritance
class BankAcct(Money):

    # Initialize variables 'name', 'account_number', 'amount', and 'interest_rate'
    def __init__(self, name, account_number, amount, interest_rate):

        # Assign 'self.name' to variable 'name'
        self.name = name

        # Assign 'self.account_number' to variable 'account_number'
        self.account_number = account_number

        # Assign 'self.amount' to variable 'amount' and convert it to a Decimal
        self.amount = Decimal(amount)

        # Assign 'self.interest_rate' to variable 'interest_rate' and convert it to a Decimal
        self.interest_rate = Decimal(interest_rate)

    # Define __str__(self) to display 'name', 'account_number', 'amount', and 'interest_rate' in a formatted manner
    def __str__(self):

        # Return a formatted string containing key variables 'name', 'account_number', 'amount', and 'interest_rate'
        return (f'Hello {self.name} \nYour Account Number is {self.account_number} '
                f'\nYour Balance is {self.amount} \nYour Interest Rate is {self.interest_rate}')

    # Define a method to change the interest rate named 'adjust_interest'
    def adjust_interest(self):

        # Set variable 'adj_int' equal to the input that the user wishes to
        # change their interest rate to (convert it to a Decimal)
        adj_int = Decimal(input(f'{self.name.title()}, 'f'Please enter the amount of interest '
                                f'you would like on your account: '))

        # If/else statement, if adj_int is less than 0 or greater than 1.0
        if adj_int <= 0 or adj_int > 1.0:

            # Print statement to let the user know the limitations to interest rates
            print('Your Interest Rate cannot be greater than 100% or lower than 0%.')

        # If/else statement, else (the value of adj) int falls within 0 to 1.0
        else:

            # Print statement to inform the user that their Interest Rate has been updated
            print('Your Interest Rate has been updated.')

            # Set 'self.interest_rate' equal to 'adj_int' to update the account
            self.interest_rate = adj_int

        # Return a formatted string that displays the updated Interest Rate
        return 'Your Interest Rate is now: ' + str((self.interest_rate)*100) + '%'

    # Define a method to calculate the accrued Interest within an entered amount of days
    def show_interest_prediction(self):

        # Set variable 'p' equal to 'self.amount', convert it to a Decimal if necessary
        p = Decimal(self.amount)

        # Set variable 'r' equal to 'self.interest_rate', convert it to a Decimal if necessary
        r = Decimal(self.interest_rate)

        # Set variable "t" equal to the input from the user dictating the number of days
        # they wish to calculate interest for, convert it to a Decimal if necessary
        t = Decimal(input("Enter the amount of days that you wish to calculate interest for: "))

        # Set variable 'simple_interest' equal to equation (p * t * r)/100 ('principle' * 'time' * 'interest rate')/100
        simple_interest = (p * t * r)/100

        # If/else statement, if their current balance is at or below zero print a statement
        # to let them know they are not eligible for interest
        if p <= 0:

            # Return string to inform user of the ineligibility of interest
            return 'Your account is not eligible for interest at this time.'

        # If/else statement, if the user's account balance is not negative or zero,
        # return a formatted string with the calculated interest
        else:

            # Return a formatted string with the calculated interest for their account
            return (f'The Calculated Simple Interest Based on Your Current Balance and '
                    f'Interest Rate is ${simple_interest:.2f}')

    # Define a method that will return the balance of the user's account
    def balance(self):

        # Return a formatted string displaying the current balance on the user's account
        return f'Your Balance is: ${self.amount}'


# Define function 'main'
def main():

    # Declare variable 'test' as a global variable
    global test

    # Print statement greeting the user
    print('Hello! Welcome to the Bank Home Page')

    # Set variable 'name' equal to a string from the user declaring their name
    name = input('What is your name? ')

    # Set variable 'account' equal to a string from the user declaring their account number
    # (up to 9 digits parameter just for flair, not implemented in any way)
    account = input('What is your account number? (up to 9 digits): ')

    # Set variable 'account' equal to a string from the input of the
    # user declaring the amount in their account converted to a Decimal
    amount = Decimal(input('What is the amount in your account? '))

    # Set variable 'interest' equal to a string from the user declaring their interest rate
    interest = input('What is your interest rate? ')

    # Set 'test' equal to class 'BankAcct' with the above variables passed in
    test = BankAcct(name=name, account_number=account, amount=amount, interest_rate=interest)

    # Print 'test' to user to display 'general info' about their account
    print(test)


# Call 'main'
main()


# Define function 'test_func' to test class 'BankAcct(Money)'
def test_func():

    # Print multiple strings that outline the services offered
    print('Please Make a Selection for Our Services'
          '\n1 - Adjust Interest Rate '
          '\n2 - Calculate Interest '
          '\n3 - Deposit Funds '
          '\n4 - Withdraw Funds'
          '\n5 - View Balance '
          '\n6 - General Account Info'
          '\n7 - Exit ')

    # Set variable 'selection' equal to the inputted value from the user (to make a selection from the given options)
    selection = input('Enter the corresponding number to the services you require: ')

    # If/elif/else statement, if 'selection' is '1' call the interest rate method
    if selection == '1':

        # Print the 'interest_rate' method
        print(test.adjust_interest())

    # Elif statement, if 'selection' is '2' call the interest prediction method
    elif selection == '2':

        # Print the 'show_interest_prediction' method
        print(test.show_interest_prediction())

    # If/elif/else statement, if 'selection' is '1' call the 'add' method
    elif selection == '3':

        # Set variable 'v' equal to a string converted to a 'Decimal' that specifies how much the user would like to
        # add to the existing amount of money
        v = Decimal(input("Enter the amount you would like to add: "))

        # Print the result of variable 'test' added to variable 'v' through the 'add' method
        test.amount += v
        print(test.amount)

    # Elif statement, if 'selection' is '4' call the 'sub' method
    elif selection == '4':

        # Set variable 'v' equal to a string converted to a 'Decimal' that specifies how much the user would like to
        # subtract from the existing amount of money
        v = Decimal(input("Enter the amount you would like to subtract: "))

        # Print the result of variable 'v' subtracted from variable 'test' through the 'sub' method
        test.amount -= v
        print(test.amount)

    # Elif statement, if 'selection' is '5' call the 'balance' method
    elif selection == '5':

        # print the 'balance' method
        print(test.balance())

    # Elif statement, if 'selection' is '6' print 'test' and show the general info for the account
    elif selection == '6':

        # Print 'test'
        print(test)

    # Elif statement, if 'selection' is '7' exit the program
    elif selection == '7':

        # Exit the program
        exit()

    # Else statement, print 'That is not a valid selection and restart the test function
    else:

        # Print 'That is not a valid selection'
        print('That is not a valid selection')

        # Call 'test_func'
        test_func()
    # Call 'test_func'
    test_func()


# Call 'test_func'
test_func()
