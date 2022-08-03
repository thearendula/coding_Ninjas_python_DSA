"""

For N = 7

*
 * *
  * * *
   * * * *
  * * *
 * *
*

"""

n = int(input())
n1 = (n+1)//2
i = 1
while(i<=n1):
    spaces = 1
    while(spaces<=i-1):
        print(" ",end="")
        spaces = spaces + 1
    p = 1
    while(p<=i):
         print("* ",end="")
         p = p + 1
    print()
    i = i + 1
n2 = n//2
i = 1
while(i<=n2):
    spaces = 1
    while(spaces<=n2-i):
        print(" ",end="")
        spaces = spaces + 1
    p = 1
    while(p<=n2-i+1):
        print("* ",end="")
        p = p + 1
    print()
    i = i + 1
