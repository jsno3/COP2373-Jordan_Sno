
from decimal import Decimal

class Money(Decimal):

    def __new__(cls, v, units='USD'):

        return super(Money, cls).__new__(cls, v)

    def __init__(self, v, units='USD'):

        self.units = units

    def addition(self):


    def subtraction(self):


    def multiplication(self):




m = Money('0.11', 'USD')
print(m, m.units)
