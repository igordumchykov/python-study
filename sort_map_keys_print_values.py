#! venv1/bin/python3

# arr = list(map(int, "2 3 6 6 5".split()))
# arr=set(arr)
# arr=sorted(arr, reverse=True)
# print(arr[1])

names = ["Harry", "Berry", "Tina", "Akriti", "Harsh"]
scores = [37.21, 37.21, 37.2, 41, 39]

# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     arr.append([name, score])
arr = []
for k, v in zip(names, scores):
    arr.append([k, v])

# arr.sort(key=lambda x: x[1])
# arr.remove(min(arr, key=lambda x: x[1]))

d = dict(zip(map(lambda x: x[0], arr), map(lambda x: x[1], arr)))

new_arr = {}
for key in set(d.values()):
    new_arr[key] = [k for k, v in d.items() if v == key]

new_arr = sorted(new_arr.items())[1][1]

for name in sorted(new_arr):
    print(name, )
