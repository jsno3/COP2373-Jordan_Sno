
from decimal import Decimal

class Money(Decimal):

    def __new__(cls, v, units='USD'):

        return super(Money, cls).__new__(cls, v)

    def __init__(self, v: Decimal, units='USD'):

        self.units = units
        self.v = v

    def __str__(self):
        return f'You have {self.v:.2f} {self.units}'

    def __add__(self, value):
        self.v += value
        return self

    def __sub__(self, value):
        self.v -= value
        return self

    def __mul__(self, value):
        self.v *= value
        return self

    def __truediv__(self, value):
        self.v /= value
        return self

def main():

    # Declare variable 'test' as a global variable
    global test

    # Print statement greeting the user
    print('Hello! Welcome to the Money Moves Program!')

    # Set variable 'name' equal to a string from the user declaring their name
    v = Decimal(input('How much money do you have? '))

    # Set variable 'account' equal to a string from the user declaring their account number
    # (up to 9 digits parameter just for flair, not implemented in any way)
    # units = input('What units do you want to use our program in? ')

    # Set 'test' equal to class 'Money' with the above variables passed in
    test = Money(v=v, units='USD')

    # Print 'test' to user to display 'general info' about their account
    print('You are starting with', test)


main()


def test_func():

    # Print multiple strings that outline the services offered
    print('Please Make a Selection for Our Services'
          '\n1 - Addition '
          '\n2 - Subtraction '
          '\n3 - Multiplication '
          '\n4 - Division'
          '\n5 - View Amount \n6 - Exit ')

    # Set variable 'selection' equal to the inputted value from the user (to make a selection from the given options)
    selection = input('Enter the corresponding number to the services you require: ')

    # If/elif/else statement, if 'selection' is '1' call the add method
    if selection == '1':

        # Print the 'add' method
        x = Decimal(input("Enter the amount you would like to add: "))
        print(test + x)

    # Elif statement, if 'selection' is '2' call the sub method
    elif selection == '2':

        # Print the 'sub' method
        x = Decimal(input("Enter the amount you would like to subtract: "))
        print(test - x)

    # Elif statement, if 'selection' is '3' call the 'mul' method
    elif selection == '3':

        # Print the 'mul' method
        x = Decimal(input("Enter the amount you would like to multiply your money by: "))
        print(test * x)

    # Elif statement, if 'selection' is '4' call the 'truediv' method
    elif selection == '4':

        # Print the 'truediv' method
        x = Decimal(input("Enter the amount you would like to divide your money by: "))
        print(test / x)
    # Elif statement, if 'selection' is '5' print 'test' and show the general info for the account
    elif selection == '5':

        # Print 'test'
        print(test)

    # Elif statement, if 'selection' is '6' exit the program
    elif selection == '6':

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
