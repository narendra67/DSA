def gcd(a, b):
    while a % b != 0:
        old_a = a
        old_b = b
        a = b
        b = old_a % old_b
    return b


class Fraction():
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, otherFraction):
        new_num = self.num * otherFraction.den + otherFraction.num * self.den
        new_den = otherFraction.den*self.den
        divisor = gcd(new_num, new_den)
        return str(new_num//divisor) + '/' + str(new_den//divisor)

    def __eq__(self, otherFraction):
        return self.num*otherFraction.den == otherFraction.num*self.den


f1 = Fraction(8, 3)
f2 = Fraction(8, 3)
print(f2, f1)
print(f2, '+', f1, '=', f2+f1)
print(f2 == f1)
