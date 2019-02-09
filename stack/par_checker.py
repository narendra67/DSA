"""Check whether the paranthesis are matching or not."""
from stack import Stack


def par_checker(paranthesis):
    open_par = '({['
    closed_par = ')}]'

    s = Stack()

    for idx, par in enumerate(paranthesis):
        if par in open_par:
            s.push(par)
        else:
            if s.size() == 0:
                return "Paranthesis wont match."
            closed_par_idx = closed_par.index(par)
            top_ele_idx = open_par.index(s.peek())
            print(closed_par_idx, top_ele_idx)
            if closed_par_idx == top_ele_idx:
                s.pop()
            else:
                return "Paranthesis wont match.."

    print(s.size(), s.peek())
    if s.size() == 0:
        return "Paranthesis match each other."
    else:
        return"Paranthesis wont match..."""