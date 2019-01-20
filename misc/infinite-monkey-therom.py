import random


def generateString(str_len):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    str = ''
    for i in range(str_len):
        str += random.choice(alphabet)
    # print(str)
    return str


def calcScore(goal_str, test_string):
    num_same = 0
    for i in range(len(goal_str)):
        if goal_str[i] == test_string[i]:
            num_same += 1

    return num_same/len(goal_str)

# calcScore('methinks it is like a weasel', generateString(28))


def main():
    goal_string = 'methinks it is like a weasel'
    new_string = generateString(28)
    no_iters = 0
    i = 1
    best_score = 0
    best_string = ''
    new_score = calcScore(goal_string, new_string)

    while new_score < 1:
        no_iters += 1
        # print(new_score, new_string)
        if new_score > best_score:
            best_score = new_score
            best_string = new_string
            print('----------->', new_score, new_string)
        if no_iters % 100000 == 0:
            i += 1
            print(no_iters)
            print(best_score, best_string)
            print(new_score, new_string)

        new_string = generateString(28)
        new_score = calcScore(goal_string, new_string)


main()