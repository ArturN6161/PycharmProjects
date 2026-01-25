class Calculator:
    def __init__(self, result, a, b, action=''):
        self.result = None
        self.action = action
        self.a = 12
        self.b = 3


    def sum(self, a, b):
        self.action = sum().__name__
        return a + b


    def different(self, a, b):
        return a - b


    def product(self, a, b):
        return a * b


    def quotient(self, a, b):
        return a / b


    def get_info(self, a, b, action, result):
        print(f'{self.action} numbers: {self.a}, {self.b} is {self.result}')

calc = Calculator(12, 3)
calc.sum()
calc.get_info()