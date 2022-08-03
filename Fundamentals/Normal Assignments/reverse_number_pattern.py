"""

1
21
321
4321
54321
654321

"""

n = int(input())
i = 1

while i <= n:
    j = 1
    p = i
    while j <= i:
        print(p, end="")
        p = p - 1
        j = j + 1
    print()
    i = i + 1
