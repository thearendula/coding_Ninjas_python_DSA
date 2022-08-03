def checkPalindrom(n):

    n = str(n)
    temp = str(n[::-1])
    if temp == n:
        return True
    else:
        return False


n = int(input())

res = checkPalindrom(n)
if res:
    print('true')
else:
    print('false')
