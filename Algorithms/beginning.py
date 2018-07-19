import math


class GCD:
    """ This class will calculate
    GCD of given two numbers.
    If the input is negative, both the
    numbers are converted to positive
    before the calculation
    """
    def __init__(self, method='euclid'):
        self.method = {
            'euclid': self._euclid,
            'stain': self._stain
        }
        self.method_type = method

    def get(self, a, b):
        try:
            a, b = abs(a), abs(b)
            return self.method[self.method_type](a, b)
        except KeyError:
            return None

    def _euclid(self, a, b):
        """
        Euclid GCD algorithm implementation.
        """
        while a % b != 0:
            old_a = a
            old_b = b

            a = old_b
            b = old_a % old_b
        return b

    def _stain(self, a, b):
        """
        Stain's GCD algorithm implementation.
        Recursive and faster that Euclid's implementation.
        """
        if a == b:
            return a
        elif a == 0:
            return b
        elif b == 0:
            return a
        # u is even
        elif a & 1 == 0:
            # v is even
            if b & 1 == 0:
                return 2 * self._stain(a >> 1, b >> 1)
            # v is odd
            else:
                return self._stain(a >> 1, b)
        # u is odd
        elif a & 1 != 0:
            # v is even
            if b & 1 == 0:
                return self._stain(a, b >> 1)
            # v is odd and u is greater than v
            elif a > b and b & 1 != 0:
                return self._stain((a - b) >> 1, b)
            # v is odd and u is smaller than v
            else:
                return self._stain((b - a) >> 1, a)


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
    gcd = GCD('euclid')
    print(gcd.get(40,15))
