n, m = input().strip().split()
n, m = [int(n), int(m)]
arr = []
for arr_i in range(n):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)
k = int(input().strip())

for arr_i in sorted(arr, key=lambda row: row[k]):
    print(' '.join(str(i) for i in arr_i ))
