stud, sub = input().strip(' ').split()
stud, sub = [int(stud), int(sub)]

arr = []
for _ in range(sub):
    arr.append(map(float, input().split()))

for i in list(zip(*arr)):
    print(sum(i) / len(i))
