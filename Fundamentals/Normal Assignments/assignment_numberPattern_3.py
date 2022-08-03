"""

for n = 4

1
11
121
1221


"""

n = int(input())

for i in range(1, n+1):

    for j in range(1, i+1):
        if j == 1 or j == i:
            if i == 1:
                print(i, end="")
            else:
                print(1, end="")
        else:
            print("2", end="")
    print()
