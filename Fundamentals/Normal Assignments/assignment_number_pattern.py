"""

For N = 4

1      1
12    21
123  321
12344321

"""

n = int(input())
i = 1

# First numbers
while i <= n:
    j = 1
    while j <= i:
        print(j, end='')
        j += 1
    spaces = 1
    while spaces <= (2*n - 2*i):
        print(' ', end='')
        spaces += 1
    p = i
    while p >= 1:
        print(p, end='')
        p -= 1
    print()
    i += 1
