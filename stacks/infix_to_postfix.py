"""Convert infix expression to postfix expression."""
from stack import Stack


def infix_to_postfix(infix_exp):
    """Concert infix to postfix.

    Convert an infix expression(string) to postfix expression using Stack.

    Parameters
    ----------
    infix_exp : string

    Return
    ------
    postfix_exp: string
    """

    s = Stack()
    post_array = []
    in_array = infix_exp.split() if ' ' in infix_exp else list(infix_exp)
    print(in_array)
    precedence = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}

    for element in in_array:
        if element not in '(*/+-)':
            post_array.append(element)
        elif element == '(':
            s.push(element)
        elif element in '*/+-':
            if (not s.is_empty()) and \
                  (precedence[element] <= precedence[s.peek()]):
                    post_array.append(s.pop())
            s.push(element)
        elif element == ')':
            while s.peek() != '(':
                post_array.append(s.pop())
            s.pop()

    while not s.is_empty():
        print('final check')
        post_array.append(s.pop())

    return "".join(post_array)
