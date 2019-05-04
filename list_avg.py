def avg(some_list: list) -> float:
    return sum(some_list) / float(len(some_list))


arr = [1, 2, 3, 4, 5, 6]
print("%.2f" % avg(arr))
