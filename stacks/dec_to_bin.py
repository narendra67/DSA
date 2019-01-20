"""Convert a decimal number to binary number."""
from stack import Stack


def dec_to_bin(dec_num):
    s = Stack()
    bin_num = ''
    while dec_num > 0:
        print(dec_num, dec_num % 2)
        s.push(dec_num % 2)
        dec_num //= 2

    while s.size():
        bin_num += str(s.pop())

    return bin_num
