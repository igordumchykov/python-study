#! venv/bin/python3.6
import copy
import string
import sysconfig

import sys


def my_sort(arr):
    return arr[1]


def safe_delete(arr, elem):
    if elem in arr:
        ind = arr.index(elem)
        del arr[ind]
    else:
        print('no such element ', elem)


def safe_delete_if_double(arr, elem):
    if elem in arr:
        ind = arr.index(elem)
        if elem in arr[ind + 1:]:
            del arr[ind]
    else:
        print('no such element ', elem)


def delete_semicolumns(x):
    for i in x:
        i = i.replace("\"", "")
        print(i)


def last_char(word):
    return word.rfind("p")


def remove_negative(arr):
    for i, n in enumerate(arr):
        if n < 0:
            arr.remove(n)
    return arr


def remove_negative_gen(arr):
    return [item for item in arr if item > -1]


def even_range(from_item, to_item):
    return (item for item in range(from_item, to_item) if item % 2 != 0)


def create_cubic_dict(from_item, to_item):
    return {item: item ** 3 for item in range(from_item, to_item)}


def func_with_many_params(x, y, **others):
    print("x: {0}, y: {1}, others: {2}".format(x, y, list(others.keys())))


def print_reversed_args(*args):
    args = list(args)[::-1]
    print(args)


def n_gen(start, end):
    while start <= end:
        yield start
        start += 1


def wc(file_path):
    """hello"""
    char_count = 0
    for file in open(file_path):
        lines = file.split('\n')
        for line in lines:
            char_count += len(line)
    print("file {0} has {1} chars".format(file_path, char_count))


def simple_decorator(func):
    print("In decorator for func {0}".format(func.__name__))

    def wrapper(*args):
        print("Executing", func.__name__)
        return func(args)

    return wrapper(func)


@simple_decorator
def logged_sum(a):
    print(a)


if __name__ == '__main__':
    x = "cwknwcnnwcrejected"
    # print(x.endswith("rejected"))

    x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
    delete_semicolumns(x)

    ind = last_char("Mississippi")
    word = "Mississippi"
    print(word[:ind] + word[ind + 1:])

    x = "%(a).08f" % {'a': 1.1111}

    text = 'this Is some text, and I know it, and you know it and everybody know it'
    text_arr = text.lower().replace(',', '').split()
    print(text_arr, sep='\n')

    counter_dict = {}
    for word in text_arr:
        if word in counter_dict:
            counter_dict[word] += 1
        else:
            counter_dict[word] = 1

    counter_dict = sorted(counter_dict.items(), key=lambda item: item[1], reverse=True)

    print(counter_dict)

    x = [1, 3, 5, 0, -1, 3, -2]
    print(remove_negative_gen(x))

    # for item in even_range(1, 100):
    #     print(item, sep=' ')

    print(create_cubic_dict(11, 15))

    wc("../hello.txt")

    print(wc.__doc__)

    func_with_many_params(y=5, x=7, foo=1, bar=2)

    print_reversed_args(1, 2, 3)

    for i in n_gen(5, 10):
        print(i)

    print(locals())

    print(globals())

    for p in sys.path:
        print(p)
