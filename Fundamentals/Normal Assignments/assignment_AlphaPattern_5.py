"""

Pattern for N = 3

A
BB
CCC

"""

n = int(input())
i = 1

ptr = ord(chr(n + 64))
k = ord(chr(ptr - n))

while i <= n:
    k = k + 1
    j = 1
    while j <= i:
        print(chr(k), end="")
        j += 1
    print()
    i += 1
