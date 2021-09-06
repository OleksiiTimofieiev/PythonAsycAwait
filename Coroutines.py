def subgen():
    message = yield
    print('Subgen received: ', message)


def coroutine(func):
    print('here 4')

    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        print('here 5')

        return g
    return inner

@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            print('here 1')
            x = yield average
            print('here 2')

        except StopIteration:
            print('-------------')
            break
        else:
            print('here 3')

            count += 1
            summ += x
            average = round(summ/count, 2)

    return average