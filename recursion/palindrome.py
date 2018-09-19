"""
    1. Base case: if string is empty or string is of length 1, its a palindrome
    2. recursive case: compare first and last word of the string. If they are 
        equal , strip them off and send the remaining string to function. Else
        return "not a palindrome".
"""


def palindrome(string):
    if len(string) == 0 or len(string) == 1:
        return "It is a palindrome"
    if string[0] == string[-1]:
        print(string[slice(1, -1)])
        return palindrome(string[slice(1, -1)])
    else:
        return "Not a palindrome"