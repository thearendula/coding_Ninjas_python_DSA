"""

A
BC
CDE
DEFG

"""
n = int(input())
i = 1

while i <= n:
    j = i + 1
    ptr = ord("A")
    while j > 1:
        print(chr(ptr + i - 1), end=" ")
        ptr = ptr + 1
        j = j - 1
    print()
    i = i + 1
