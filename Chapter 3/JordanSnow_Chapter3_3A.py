# Explanation

import functools

print("Welcome to the Expense Calculator!")
expenses_inputted = input("Do you have any expenses to enter? ")





def max_function(current_max, max_candidate):
    if current_max[1] < max_candidate[1]:
        return max_candidate
    else:
        return current_max


def min_function(current_min, min_candidate):
    if min_candidate[1] < current_min[1]:
        return min_candidate
    else:
        return current_min



def get_expense():
    expense_type = input("Enter the type of expense (rent, insurance, food, etc.) ")
    expense_amount = input("Enter amount of expenses ")
    return expense_type, float(expense_amount)


def main():

