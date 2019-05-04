def swap_case(input_str):
    return input_str.swapcase()


def split_and_join(input_str: str, split_del: str, join_del: str) -> str:
    return join_del.join(input_str.split(split_del))


def print_full_name(a, b):
    print("Hello {0} {1}! You just delved into python.".format(a,b))


def mutate_string(string, position, character):
    return string[:position:] + character + string[position+1::]


if __name__ == '__main__':
    print(swap_case('Hello'))
    print(split_and_join("hello my name is Igor", " ", "-"))
    print_full_name("Igor", "Dumchykov")
    print(mutate_string("hello", 3, "A"))
