def function_mapping(arr: list, cmd: str, args):
    if cmd == 'insert':
        # print(command, "->", args[0], args[1])
        arr.insert(args[0], args[1])
    elif cmd == 'remove':
        arr.remove(args[0])
    elif cmd == 'append':
        arr.append(args[0])
    elif cmd == 'sort':
        arr = sorted(arr)
    elif cmd == 'reverse':
        arr = list(reversed(arr))
    elif cmd == 'pop':
        arr.pop()
    else:
        print(arr)
    return arr


test_list = []
for _ in range(int(input())):
    command, *args = input().split()
    args = list(map(int, args))
    test_list = function_mapping(test_list, command, args)
