"""Convert decimal number to anybase."""
from stack import Stack


def dec_to_any_base(dec_num, base):
    """Convert a decimal number to the base provided."""

    digits = '0123456789ABCDEF'
    s = Stack()
    new_num = ''

    while dec_num > 0:
        s.push(dec_num % base)
        dec_num //= base

    while s.size():
        new_num += str(digits[s.pop()])

    return new_num
