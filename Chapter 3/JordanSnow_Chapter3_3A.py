# Explanation

import functools


class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f'{self.name}: ${self.amount:.2f}'


def get_expense():
    expense_type = input("Enter the type of expense (Rent, Insurance, Food, Etc.) ")
    expense_amount = input("Enter amount of expense ")
    return Expense(expense_type, float(expense_amount))

def total_function(cum, next_number):
    return cum + next_number


def min_function(current_min, min_candidate):
    if min_candidate.amount < current_min.amount:
        return min_candidate
    else:
        return current_min


def max_function(current_max, max_candidate):
    if current_max.amount < max_candidate.amount:
        return max_candidate
    else:
        return current_max


def main():
    print("Welcome to the Expense Calculator!")
    print("Please enter in your monthly expenses, one at a time.")

    expenses = []
    complete = False

    while not complete:
        expenses.append(get_expense())

        more_expenses = input("input another expense? (y/n) ")

        if more_expenses not in ['Y', 'y']:
            complete = True

    total_expense = functools.reduce(total_function, [expense.amount for expense in expenses])
    highest_expense = functools.reduce(max_function, expenses)
    lowest_expense = functools.reduce(min_function, expenses)
    print(f"Your combined expenses are: ${total_expense:.2f}")
    print("Your highest expense is", highest_expense)
    print("Your lowest expense is", lowest_expense)


main()
