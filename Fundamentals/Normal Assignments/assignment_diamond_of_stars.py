"""

N = 5

   *
  ***
 *****
  ***
   *

"""
n=int(input())
n1=(n+1)//2
n2=n-n1
for i in range(1,n1+1):
    for j in range(n1-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
for i in range(1,n2+1):
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(1,2*(n2-i+1)):
        print("*",end="")
    print()
