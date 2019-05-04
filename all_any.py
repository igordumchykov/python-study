
if __name__ == '__main__':
    n = int(input())
    arr_str = input()
    arr_int = list(map(int, arr_str))

    if all(i >= 0 for i in arr_int):
        if any(el == el[::-1] for el in arr_str):
            print(True)
