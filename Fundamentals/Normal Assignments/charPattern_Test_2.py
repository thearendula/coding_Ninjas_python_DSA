"""

n = 5

E
DE
CDE
BCDE
ABCDE

"""
n = int(input())
i = 1

while i <= n:
    j = i + 1
    ptr = ord(chr(n + 64))
    k = ptr - i
    while j > 1:
        print(chr(k + 1), end="")
        k = k + 1
        j = j - 1
    print()
    i = i + 1

# Coding Ninjas Code

# n1 = int(input())
# currRow = 1
#
# while currRow <= n1:
#     currCol = 1
#
#     ch = ord('A') + n1 - currRow
#     print("Outer CH : ", ch)
#     while currCol <= currRow:
#         print(chr(ch + currCol - 1), end="")
#         currCol += 1
#
#     print()
#     currRow += 1
