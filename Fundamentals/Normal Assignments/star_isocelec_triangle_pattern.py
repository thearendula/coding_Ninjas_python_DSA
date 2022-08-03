"""
    *
   ***
  *****
 *******

CODING NINJA SOLUTION

n = int(input())
currRow = 1

while currRow <= n:
    s = 1
    while s <= n - currRow:
        print(' ', end='')
        s += 1
    currCol = 1
    while currCol <= ((2 * currRow) - 1):
        print("*", end='')
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
    # Printing Increasing number
    p = 1
    j = 1
    while j <= i:
        print('*', end='')
        j += 1
        p += 1
    # Printing Decreasing number
    p = i - 1
    while p >= 1:
        print('*', end='')
        p -= 1
    print()
    i += 1
