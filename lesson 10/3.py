class Cell():
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        self.quantity += other.quantity

    def __sub__(self, other):
        if self.quantity < other.quantity:
            return "Second cell bigger"
        else:
            self.quantity -= other.quantity

    def __mul__(self, other):
        self.quantity *= other.quantity

    def __floordiv__(self, other):
        self.quantity = self.quantity // other.quantity

    def __truediv__(self, other):
        self.quantity = self.quantity // other.quantity

    def make_order(self, num):
        full_rows = self.quantity // num
        remainder = self.quantity % num
        return (("*" * num) + "\n") * full_rows + "*" * remainder