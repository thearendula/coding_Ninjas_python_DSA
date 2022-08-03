"""

Pattern for N = 4

1
11
202
3003

"""

n = int(input())

for i in range(1, n+1):

    for j in range(1, i+1):
        if j == 1 or j == i:

            if i == 1:
                print(i, end="")

            else:
                print(i-1, end="")

        else:
            print("0", end="")

    print()
