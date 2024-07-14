""" The purpose of this program is to create a class named "Money" that inherits "Decimal"
and expand upon its functionality. The class has been extended to support basic addition,
subtraction, multiplication, and division. Also, two functions 'main' and 'test_func' have been
added to work in conjunction with one another to test the class's functionality and methods.
"""

# Import Decimal from decimal
from decimal import Decimal


# Define class "Money" that inherits "Decimal"
class Money(Decimal):

    # Use __new__ to call the superclass version of __new__, pass in 'cls' to reference the class,
    # 'v' to reference the amount of money, and "units='USD'" to assign 'USD' to the money in said class
    def __new__(cls, v, units='USD'):

        # return the superclass version of __new__
        return super(Money, cls).__new__(cls, v)

    # Initialize variables 'v' and 'units'
    def __init__(self, v: Decimal, units='USD'):

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

    # Define __mul__ passing in 'self' and 'value'
    def __mul__(self, value):

        # Multiply variables 'self.v' and 'value' and set 'self.v' equal to the result
        self.v *= value

        # Return the value of 'self'
        return self

    # Define __truediv__ passing in 'self' and 'value'
    def __truediv__(self, value):

        # Divide variable 'self.v' by variable 'value' and set 'self.v' equal to the result
        self.v /= value

        # Return the value of 'self'
        return self


# Define main
def main():

    # Declare variable 'test' as a global variable
    global test

    # Print statement greeting the user
    print('Hello! Welcome to the Money Program!')

    # Set variable 'v' equal to a string converted to a 'Decimal' from the user entering how much money they have
    v = Decimal(input('How much money do you have? '))

    # Set 'test' equal to class 'Money' with the 'v' passed in and 'units' set to 'USD'
    test = Money(v=v, units='USD')

    # Print 'test' to user to display how much money they have
    print(test)


# Call main
main()


# Define test_func
def test_func():

    # Print multiple strings that outline the methods available in this program
    print('List of options for Money Program:'
          '\n1 - Addition '
          '\n2 - Subtraction '
          '\n3 - Multiplication '
          '\n4 - Division'
          '\n5 - View Amount \n6 - Exit ')

    # Set variable 'selection' equal to the inputted value from the user (to make a selection from the given options)
    selection = input('Please make a selection (enter numbers 1-6): ')

    # If/elif/else statement, if 'selection' is '1' call the add method
    if selection == '1':

        # Set variable 'v' equal to a string converted to a 'Decimal' that specifies how much the user would like to
        # add to the existing amount of money
        v = Decimal(input("Enter the amount you would like to add: "))

        # Print the result of variable 'test' added to variable 'x' through the 'add' method
        print(test + v)

    # Elif statement, if 'selection' is '2' call the sub method
    elif selection == '2':

        # Set variable 'v' equal to a string converted to a 'Decimal' that specifies how much the user would like to
        # subtract from the existing amount of money
        v = Decimal(input("Enter the amount you would like to subtract: "))

        # Print the result of variable 'x' subtracted from variable 'test' through the 'sub' method
        print(test - v)

    # Elif statement, if 'selection' is '3' call the 'mul' method
    elif selection == '3':

        # Set variable 'v' equal to a string converted to a 'Decimal' that specifies how much the user would like to
        # multiply their existing amount of money by
        v = Decimal(input("Enter the amount you would like to multiply your money by: "))

        # Print the result of variable 'test' multiplied by variable 'v' through the 'mul' method
        print(test * v)

    # Elif statement, if 'selection' is '4' call the 'truediv' method
    elif selection == '4':

        # Set variable 'v' equal to a string converted to a 'Decimal' that specifies how much the user would like to
        # divide their existing amount of money by
        v = Decimal(input("Enter the amount you would like to divide your money by: "))

        # Print the result of variable 'test' divided by variable 'v' through the 'truediv' method
        # (I used 'truediv' for better results with decimals and rounding)
        print(test / v)

    # Elif statement, if 'selection' is '5' print 'test' and show the user how much money they have
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
