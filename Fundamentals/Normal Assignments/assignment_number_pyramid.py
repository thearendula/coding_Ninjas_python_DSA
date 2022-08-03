"""

for n = 4

1234
 234
  34
   4
  34
 234
1234

"""
n = int(input())

n1 = n
n2 = n - 1

for i in range(1, n1+1):
    for space in range(1, i):
        print(' ', end='')
    for number in range(i, n1+1):
        print(number, end='')
    print()
for j in range(2, n+1):
    for space1 in range(1, n-j+1):
        print(' ', end='')
    for num1 in range(j, 0, -1):
        print(n-num1+1, end='')
    print()
