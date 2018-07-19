class GCD:

    def __init__(self, method='euclid'):
        self.method = method

    def get(self, num1, num2):
        return self.__dict__[f'_{self.method}'](num1, num2)

    def _euclid(self, num1, num2):
        pass

    def _stain(self, num1, num2):
        pass


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'


if __name__ == '__main__':
    fr1 = Fraction(3, 5)
    fr2 = Fraction(1, 5)
    print(fr1 + fr2)
