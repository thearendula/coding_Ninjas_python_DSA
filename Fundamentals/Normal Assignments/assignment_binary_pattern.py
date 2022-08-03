"""

for n = 4

1111
000
11
0

"""
n = int(input())

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        if i % 2 == 0:
            print('1', end='')
        else:
            print('0', end='')
    print()

n=int(input())
for i in range(1,n+1,1):
    j=1
    while j<=n-i+1:
        if(i==1 or i%2==1):
            print('1',end='')
        else:
            print('0',end='')
        j=j+1
    print()
    i=i+1