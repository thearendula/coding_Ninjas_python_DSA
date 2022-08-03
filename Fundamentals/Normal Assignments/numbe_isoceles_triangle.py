"""
    1
   121
  12321
 1234321

"""
n = int(input())
i = 1

while i <= n:
    # Printing Spaces
    s = 1
    while s <= n - i:
        print(' ', end='')
        s += 1
    # Printing Increasing number
    p = 1
    j = 1
    while j <= i:
        print(p, end='')
        j += 1
        p += 1
    # Printing Decreasing number
    p = i - 1
    while p >= 1:
        print(p, end='')
        p -= 1
    print()
    i += 1
