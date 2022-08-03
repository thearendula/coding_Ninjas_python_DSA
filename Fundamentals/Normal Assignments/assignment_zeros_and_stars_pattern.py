"""

for N = 4

*000*000*
0*00*00*0
00*0*0*00
000***000

"""


n = int(input())
i = 1
while i <= n:
    j = i - 1
    while j >= 1:
        print("0", end='')

        j = j - 1
    d = 1
    while d <= n - i + 1:
        if d == 1:
            print("*", end='')
        else:
            print("0", end='')
        d = d + 1
    f = i
    while f <= i:

        if f == 1 or f == i:
            print("*",end='')
        else:
            print(0,end='')
        f = f + 1
    k = 1
    while k <= n-i+1 :
        if k == n-i+1:
            print("*",end='')
        else:
            print("0",end='')
        k = k + 1

    s = i - 1
    while s >= 1:
        print("0", end='')
        s = s - 1
    print()
    i = i + 1
