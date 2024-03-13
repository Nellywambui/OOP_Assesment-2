class Calculator:
    def __int__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def sum(x,y):
        return x + y

    @staticmethod
    def subtraction(x,y):
        return x - y

    @staticmethod
    def multiplication(x,y):
        return x * y

    @staticmethod
    def division(x, y):
        return x / y

c = Calculator()
print(c.sum(4,5))
print(c.subtraction(4,5))
print(c.multiplication(4,5))
print(c.division(4,5))