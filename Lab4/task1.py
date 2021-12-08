import math


class Rational:

    def __init__(self, numerator=1, denominator=1):
        self.__numerator = numerator
        self.__denominator = denominator
        self.abbreviation()

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, numerator):
        if not numerator:
            raise TypeError
        if not isinstance(numerator, int):
            raise TypeError
        self.__numerator = numerator

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator):
        if not denominator:
            raise ZeroDivisionError
        if not isinstance(denominator, int):
            raise TypeError
        self.__denominator = denominator

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def __float__(self):
        return self.__numerator / self.__denominator

    def abbreviation(self):
        k = math.gcd(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator // k
        self.__denominator = self.__denominator // k

    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.__numerator * other.__denominator + other.__numerator * self.__denominator,
                            self.__denominator * other.__denominator)
        if isinstance(other, int):
            return Rational(self.__numerator + other * self.__denominator, self.__denominator)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Rational):
            return Rational(self.__numerator * other.__denominator + other.__numerator * self.__denominator,
                            self.__denominator * other.__denominator)
        if isinstance(other, int):
            return Rational(self.__numerator + other * self.__denominator, self.__denominator)
        else:
            raise TypeError

    def __sub__(self, other):
        assert type(other) == Rational
        new_numerator = self.__numerator * other.__denominator - self.__denominator * other.__numerator
        new_denominator = self.__denominator * other.__denominator
        return Rational(new_numerator, new_denominator)

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        assert type(other) == Rational
        new_numerator = self.__numerator * other.__numerator
        new_denominator = self.__denominator * other.__denominator
        return Rational(new_numerator, new_denominator)

    def __imul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        assert type(other) == Rational
        new_numerator = self.__numerator * other.__denominator
        new_denominator = self.__denominator * other.__numerator
        return Rational(new_numerator, new_denominator)

    def __idiv__(self, other):
        return self.__truediv__(other)

    def __eq__(self, other):
        if type(other) is not Rational:
            return False
        else:
            first_number = self.__numerator * other.__denominator
            second_number = self.__denominator * other.__numerator
            return first_number == second_number

    def __lt__(self, other):
        if not isinstance(other, Rational):
            raise Exception("Not Rational")
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        if not isinstance(other, Rational):
            raise Exception("Not Rational")
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        if not isinstance(other, Rational):
            raise Exception("Not Rational")
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        if not isinstance(other, Rational):
            raise Exception("Not Rational")
        return self.numerator * other.denominator >= other.numerator * self.denominator


class main:
    try:
        num = input('Enter numerator: ')
        denum = input('Enter denominator: ')
        my_rect = Rational(int(num), int(denum))
        print(my_rect)
        print("Result: ", float(my_rect))

        my_rect1 = Rational(3, 7)
        my_rect2 = Rational(5, 9)
        my_rect3 = my_rect1 + my_rect2
        print(f'my_rect1 + my_rect2 = {my_rect3}')

        my_rect3 += my_rect2
        print(f'my_rect3 += my_rect2 = {my_rect3}')

        my_rect3 = my_rect1 - my_rect2
        print(f'my_rect1 - my_rect2 = {my_rect3}')

        my_rect3 = my_rect1 * my_rect2
        print(f'my_rect1 * my_rect2 = {my_rect3}')

        my_rect3 = my_rect1 / my_rect2
        print(f'my_rect1 / my_rect2 = {my_rect3}')

        boolean = my_rect1 == my_rect2
        print(f'my_rect1 == my_rect2 is {boolean}')

        boolean = my_rect1 < my_rect2
        print(f'my_rect1 < my_rect2 is {boolean}')

        input('press enter to continue')
    except Exception:
        print("Exeption!")
