# Explanation

import functools


class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f'{self.name}: ${self.amount:.2f}'

def get_expense():
    expense_type = input("Enter the type of expense (rent, insurance, food, etc.) ")
    expense_amount = input("Enter amount of expenses ")
    return Expense(expense_type, float(expense_amount))


def main():
    print("Welcome to the Expense Calculator!")

    expenses = []
    complete = False

    while not complete:
        expenses.append(get_expense())

        more_expenses = input("input another expense? (y/n)\n")

        if more_expenses not in ['Y', 'y']:
            complete = True
    sec(expenses)


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


def total_function(cum: float, next_number: float):
    return cum + next_number


def sec(expenses):
    total_expense = functools.reduce(total_function, [expense.amount for expense in expenses])
    largest_expense = functools.reduce(max_function, expenses)
    smallest_expense = functools.reduce(min_function, expenses)
    print(f"Your total expenses are: ${total_expense:.2f}")
    print("Your largest expense is:", largest_expense)
    print("Your smallest expense is:", smallest_expense)


main()
