class Calculator(object):

    def __init__(self):
        self.total = 0

    def add(self, x, y = None):
        if y is None:
            self.total += x
        else:
            self.total = x + y

    def subtract(self, x, y = None):
        if y is None:
            self.total -= x
        else:
            self.total = x - y

    def multipy(self, x, y = None):
        if y is None:
            self.total *= x
        else:
            self.total = x * y

    def divide(self, x, y = None):
        if y is None:
            self.total /= x
        else:
            self.total = x / y
