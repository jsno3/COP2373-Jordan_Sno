

class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def __str__(self):
        return f'Hello {self.name} \nYour Account Number is {self.account_number} \nYour Balance is {self.amount} \nYour Interest Rate is {self.interest_rate}'
        # return f'Your Balance is {self.amount} \nYour Interest Rate is {self.interest_rate}'

    def adjust_interest(self):
        adj_int = float(input(f'{self.name.title()}, please enter the amount of interest you would like on your account: '))
        return self.interest_rate == adj_int

    def deposit(self):
        deposit = float(input(f'{self.name.title()}, please enter the amount you would like to deposit: '))
        if amount < 0:
            print("You cannot deposit a negative amount.")
        else:
            print('Thank you for your deposit!')
            self.amount += deposit
        return f'Your Balance is now: ${round(self.amount), 2}'

    def withdraw(self):
        withdraw = float(input(f'{self.name.title()}, please enter how much you would like to withdraw: '))
        if self.amount < withdraw or withdraw < 0:
            return "You cannot withdraw that amount."
        else:
            print(f'You have withdrawn ${withdraw}')
            self.amount -= withdraw
        return f'Your Balance is now: ${self.amount}'

    def balance(self):
        balance = str(input(f'{self.name.title()}, would you like to see your current Balance? (y/n): '))
        if balance == 'y' or 'Y':
            return f'Your Balance is: ${self.amount}'





test = BankAcct('Jordan', 1234, 650, '.06')
print(test)


