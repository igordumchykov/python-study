import operator
import time


def func():
    X = 'NI'

    def nested():
        nonlocal X
        X = 'Spam'

    print(X)
    nested()


def func1() -> None:
    print(func1.name)
    func1.name += "Bye!"


def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res


start = time.clock()
time.sleep(1)
print("Slept %.6f seconds" % float(time.clock() - start))