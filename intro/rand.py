def flipCoin(p):
    # YOUR CODE HERE
    if (rand() % 2 == 0) and (int(p*10) % 2 == 0):
        return 0
    else:
        return 1