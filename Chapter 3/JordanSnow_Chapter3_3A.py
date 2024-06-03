# This program is intended to ask the user for a list of their monthly expenses.
# When the user is prompted for their expenses, the program will ask for the type of expense as well as the amount of said expense.
# The program will ask the user if they have any more expenses after each entry, and will loop until they do not.
# After the user has entered all of their expenses, the program will calculate their expenses combined, their highest expense, and their lowest expense.
# Finally, the program will display all of this information to the user.

# import functools to be able to use reduce later in the program
import functools


# Create a class named "Expense"
class Expense:

    # Define class variables and pass in variables: (self, name, amount)
    def __init__(self, name, amount):

        # Create a variable "self.name"
        self.name = name

        # Create a variable "self.amount"
        self.amount = amount

    # Define string function and pass in variable "self"
    def __str__(self):

        # Return formatted version of "self.name" and "self.amount"
        return f'{self.name}: ${self.amount:.2f}'


# Define "get_expense"
def get_expense():

    # Create a variable named "expense_type" that receives an input from the user for the type of expense
    expense_type = input("Enter the type of expense (Rent, Insurance, Food, Etc.) ")

    # Create a variable named "expense_amount" that receives an input from the user for the expense amount
    expense_amount = input("Enter amount of expense ")

    # Returns a variable named "Expense" that combines "expense_type" and a float version of "expense_amount"
    return Expense(expense_type, float(expense_amount))


# Define "total_function" passing in parameters "cum" and "next_number"
def total_function(cum, next_number):

    # Return cum + next_number
    return cum + next_number


# Define "min_function" passing in parameters "current_min" and "min_candidate"
def min_function(current_min, min_candidate):

    # If the amount of "min_candidate" is less than the amount of "current_min"
    if min_candidate.amount < current_min.amount:

        # Return "min_candidate"
        return min_candidate

    # Else
    else:

        # Return "current_min"
        return current_min


# Define "max_function" passing in parameters "current_max" and "max_candidate"
def max_function(current_max, max_candidate):

    # If the amount of "current_max" is less than the amount of "max_candidate"
    if current_max.amount < max_candidate.amount:

        # Return "max_candidate"
        return max_candidate

    # Else
    else:

        # Return "current_max"
        return current_max


# Define "main"
def main():

    # Print welcome statement
    print("Welcome to the Expense Calculator!")

    # Print statement "Please enter in your monthly expenses, one at a time."
    print("Please enter in your monthly expenses, one at a time.")

    # Create a variable named "expenses" that is assigned to an empty list
    expenses = []

    # Create a variable named "complete" that is assigned to a boolean value "False"
    complete = False

    # While "complete" is "False"
    while not complete:

        # Append list "expenses" with entries from function "get_expenses"
        expenses.append(get_expense())

        # Create a variable "more_expenses" and assign it a string that the user inputs
        more_expenses = input("input another expense? (y/n) ")

        # If "more_expenses" does not contain either a "Y" or a "y"
        if more_expenses not in ['Y', 'y']:

            # Set variable "complete" to boolean value "True"
            complete = True

    # Define a variable "total_expense" and assign it the result of using the reduce method on "total_function," to sum every expense in expenses
    total_expense = functools.reduce(total_function, [expense.amount for expense in expenses])

    # Define a variable "highest_expense" and assign it the result of using the reduce method and passing in parameters "max_function" and "expenses"
    highest_expense = functools.reduce(max_function, expenses)

    # Define a variable "lowest_expense" and assign it the result of using the reduce method and passing in parameters "min_function" and "expenses"
    lowest_expense = functools.reduce(min_function, expenses)

    # Print statement to display the user's combined expenses
    print(f"Your combined expenses are: ${total_expense:.2f}")

    # Print statement to display the user's highest expense
    print("Your highest expense is", highest_expense)

    # Print statement to display the user's lowest expense
    print("Your lowest expense is", lowest_expense)


# Call main
main()
