"""
    1
   232
  34543
 4567654

CN Solution

n = int(input())
currRow = 1

while currRow <= n:
    space = 1
    while space <= (n - currRow):
    print(' ', end="")
    space += 1

    currCol = 1
    p = currRow
    while currCol <= currRow:
        print(p, end="")
        p += 1
        currCol += 1

    currCol = 1
    p = 2*currRow - 2
    while currCol <= currRow - 1:
        print(p, end="")
        currCol += 1

    print()
    currRow += 1

"""
n = int(input())
i = 1

while i <= n:
    # Printing Spaces
    s = 1
    while s <= n - i:
        print(' ', end='')
        s += 1
    # Print increasing number
    j = 1
    p = i
    while j <= i:
        print(p, end='')
        j += 1
        p += 1
    # # Print decreasing number
    p = 2*i - 2
    while p >= i:
        print(p, end='')
        p -= 1
    print()
    i += 1
