class Fibonacci:
    def calculate(self, n):
        if n < 0:
            raise ValueError("Argument less than zero")
        elif n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.calculate(n - 1) + self.calculate(n - 2)
