class Calculator:
    def add(self, n1, n2):
        return n1 + n2

    def subtract(self, n1, n2):
        return n1 - n2

    def multiply(self, n1, n2):
        return n1 * n2

    def divide(self, n1, n2):
        if n2 == 0:
            raise ValueError("Can't divide by zero")
        return n1 / n2
