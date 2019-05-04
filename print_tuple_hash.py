t_size = int(input())
arr = input().split()

arr = map(int, arr)
t = tuple(arr)

print(hash(t))