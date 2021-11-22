def print_mountain(ipt: str, depth: int):
    space = len(ipt)
    for i in range(1, depth + 1):
        for _ in range(depth - i):
            print(' ' * space, end='')

        print(ipt*(2*i-1))


while(True):
    n = int(input("Enter an integer:"))
    if n <= 0:
        break
    ipt = input("Enter a string:")
    print_mountain(ipt, n)


print("Program ends.")
