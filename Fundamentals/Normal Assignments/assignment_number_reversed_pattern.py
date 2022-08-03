"""

    1
   12
  123
 1234

CODING NINJAS SOLUTION

n = int(input())
currRow = 1

while currRow <= n:
    currCol = 1
    spaces = 1
    while spaces <= n - currRow:
        print(" ", end="")
        spaces += 1
    while currCol <= currRow:
        print(currCol, end="")
        currCol += 1
    print()
    currRow += 1

"""

n = int(input())
i = 1

while i <= n:
    space = 1
    while space <= n - i:
        print(' ', end="")
        space += 1
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1
