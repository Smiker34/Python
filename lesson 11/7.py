class Complex():
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real = str(self.real + other.real)
        imag = str(self.imag + other.imag)
        if int(imag) > 0:
            return real + "+" + imag + 'j'
        else:
            return real + imag + 'j'

    def __mul__(self, other):
        real = str(self.real * other.real - self.imag * other.imag)
        imag = str(self.real * other.imag + self.imag * other.real)
        if int(imag) > 0:
            return real + "+" + imag + 'j'
        else:
            return real + imag + 'j'