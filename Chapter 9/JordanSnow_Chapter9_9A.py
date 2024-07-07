
class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = float(amount)
        self.interest_rate = float(interest_rate)


    def __str__(self):
        return f'Hello {self.name} \nYour Account Number is {self.account_number} \nYour Balance is {self.amount} \nYour Interest Rate is {self.interest_rate}'
        # return f'Your Balance is {self.amount} \nYour Interest Rate is {self.interest_rate}'


    def adjust_interest(self):
        adj_int = float(input(f'{self.name.title()}, '
                              f'please enter the amount of interest you would like on your account: '))
        if adj_int <= 0 or adj_int > 1.0:
            print('Your Interest Rate cannot be greater than 100% or lower than 0%.')
        else:
            print('Your Interest Rate has been updated.')
            self.interest_rate = adj_int
        return f'Your Interest Rate is now: {self.interest_rate}'


    def show_interest_prediction(self):
        p = float(self.amount)
        r = float(self.interest_rate)
        t = float(input("Enter the amount of days that you wish to calculate interest for: "))
        simple_interest = (p * t * r)/100
        if p == 0:
            return 'Your account is not eligible for interest at this time.'
        else:
            return (f'The Calculated Simple Interest Based '
                    f'on Your Current Balance and Interest Rate '
                    f'is ${simple_interest}')


    def deposit(self):
        deposit = float(input(f'{self.name.title()}, please enter the amount you would like to deposit: '))
        if deposit < 0:
            return 'You cannot deposit a negative amount.'
        else:
            print('Thank you for your deposit!')
            self.amount += deposit
        return f'Your Balance is now: ${self.amount}'


    def withdraw(self):
        withdraw = float(input(f'{self.name.title()}, please enter how much you would like to withdraw: '))
        if self.amount < withdraw or withdraw < 0:
            return 'You cannot withdraw that amount.'
        else:
            print(f'You have withdrawn ${withdraw}')
            self.amount -= withdraw
        return f'Your Balance is now: ${self.amount}'


    def balance(self):
        # balance = str(input(f'{self.name.title()}, would you like to see your current Balance? (y/n): '))
        # if balance == 'y' or 'Y':
        return f'Your Balance is: ${self.amount}'


def main():
    global test
    print('Hello! Welcome to the Bank Home Page')
    name = input('What is your name? ')
    account = input('What is your account number? (up to 9 digits): ')
    amount = input('What is the amount in your account? ')
    interest = input('What is your interest rate? ')
    test = BankAcct(name=name, account_number=account, amount=amount, interest_rate=interest)
    print(test)


main()


def test_func():
    print('Please Make a Selection for Our Services'
        '\n1 - Adjust Interest Rate '
        '\n2 - Calculate Interest '
        '\n3 - Withdraw Funds \n4 - Deposit Funds'
        '\n5 - View Balance \n6 - Exit ')
    selection = input('Enter the corresponding number to the services you require: ')
    if selection == '1':
        print(test.adjust_interest())
    elif selection == '2':
        print(test.show_interest_prediction())
    elif selection == '3':
        print(test.withdraw())
    elif selection == '4':
        print(test.deposit())
    elif selection == '5':
        print(test.balance())
    elif selection == '6':
        exit()
    else:
        print('That is not a valid selection')
        test_func()
    test_func()


test_func()
