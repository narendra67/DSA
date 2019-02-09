from queue import Queue


def hot_potato(peopleList = [], num = 1):
    """A game where a potato will be passed around n number of
        people, until num - number at which the moving of potato
        should be stopped and the person holding the potato will
        be eliminated. This goes on until only one person is left.
    """
    tempQueue = Queue()

    if len(peopleList) == 0:
        return 'Number of participants should be atleast 1.'

    for name in peopleList:
        tempQueue.enqueue(name)

    while tempQueue.size() > 1:
        if num < 1:
            return 'Number (num) of iterations should be >= 1.'
        # i = 1
        # while i <= num:
        #     tempQueue.enqueue(tempQueue.dequeue())
        #     i += 1
        # else:
        #     tempQueue.dequeue()
        for i in range(num):
            tempQueue.enqueue(tempQueue.dequeue())

        tempQueue.dequeue()

    winner = tempQueue.dequeue()
    return (str(winner) if type(winner) == int else winner) + ' is the winner.'