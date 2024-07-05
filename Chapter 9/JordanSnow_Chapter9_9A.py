

class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def __str__(self):
        return f'Your Balance is {self.amount} \nYour Interest Rate is {self.interest_rate}'


test = BankAcct(name = 'Jordan', account_number = 1234, amount = 650, interest_rate = '.06')
print(test)


