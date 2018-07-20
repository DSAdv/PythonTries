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

    def __init__(self, numerator, denominator, method='euclid'):
        self.negative = False
        self.gcd = GCD(method)

        self.numerator = abs(numerator)
        self.denominator = abs(denominator)
        self.reduce()
        if numerator < 0 and denominator < 0:
            pass
        elif numerator < 0 or denominator < 0:
            self.negative = True

    def is_negative(self):
        return True if self.negative else False

    def reduce(self):
        common = self.gcd.get(self.numerator, self.denominator)
        if common > 1:
            self.numerator //= common
            self.denominator //= common

    def _execute_operation(self, other, operation=''):

        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b
        }

        fst_num = self.numerator
        snd_num = other.numerator
        new_denominator = self.denominator * other.denominator

        if operation in ['+', '-']:
            fst_num = self.numerator * other.denominator
            snd_num = other.numerator * self.denominator
        elif operation == '/':
            snd_num = other.denominator
            new_denominator = self.denominator * other.numerator
            operation = '*'

        if self.is_negative():
            fst_num = -fst_num
        if other.is_negative():
            snd_num = -snd_num

        new_numerator = operations[operation](fst_num, snd_num)

        instance = Fraction(new_numerator, new_denominator)
        instance.reduce()
        return instance

    def __neg__(self):
        self.negative = False if self.is_negative() else True
        return self

    def __add__(self, other):
        return self._execute_operation(other, operation='+')

    def __sub__(self, other):
        return self._execute_operation(other, operation='-')

    def __mul__(self, other):
        return self._execute_operation(other, operation='*')

    def __truediv__(self, other):
        return self._execute_operation(other, operation='/')

    def __eq__(self, other):
        fst_numerator = self.numerator * other.denominator
        snd_numerator = other.numerator * self.denominator
        return fst_numerator == snd_numerator and self.is_negative() == other.is_negative()

    def __ne__(self, other):
        fst_numerator = self.numerator * other.denominator
        snd_numerator = other.numerator * self.denominator
        return fst_numerator != snd_numerator

    def __str__(self):
        num, den = abs(self.numerator), abs(self.denominator)
        return f'-{num}/{den}' if self.is_negative() else f'{num}/{den}'


if __name__ == '__main__':
    fr1 = Fraction(4, 5)
    fr2 = Fraction(1, 4)
    fr3 = Fraction(2, 8)
    print(fr1/fr2)
    print(fr2 != fr1)
    print(fr2 == fr3)
    gcd = GCD('stain')
    print(gcd.get(40,15))
