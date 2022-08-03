def checkMember(n):
    f3 = 0
    f2 = 1
    f1 = 1

    if n == 0 or n == 1:
        return True
    else:
        while f3 < n:
            f3 = f1 + f2
            f2 = f1
            f1 = f3

        if f3 == n:
            return True
        else:
            return False


n = int(input())

if checkMember(n):
    print('true')
else:
    print('false')