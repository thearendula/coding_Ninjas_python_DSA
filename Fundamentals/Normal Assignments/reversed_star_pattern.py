n = int(input())
i = 1

while i <= n:
    space = 1
    while space <= n - i:
        print(' ', end="")
        space += 1
    stars = 1
    while stars <= i:
        print('*', end="")
        stars += 1
    print()
    i += 1