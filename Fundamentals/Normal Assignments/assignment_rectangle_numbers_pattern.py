"""

for n = 3

33333
32223
32123
32223
33333

"""

n = int(input())
k = (2*n) - 1

low = 0
high = k - 1
val = n

m = [[0 for i in range(k)] for j in range(k)]


for i in range(n):
    # Printing First part
    for j in range(low, high+1):
        m[i][j] = val

    # Printing Second Part
    for j in range(low+1, high+1):
        m[j][i] = val

    # Printing Third Part
    for j in range(low + 1, high + 1):
        m[high][j] = val

    # Printing Fourth Part
    for j in range(low + 1, high):
        m[j][high] = val

    low += 1
    high -= 1
    val -= 1

for i in range(k):
    for j in range(k):
        print(m[i][j], end='')
    print()
