def check_Armstrong(n):
    temp = n
    count = 0
    while temp > 0:
        count += 1
        temp = temp // 10

    sum = 0
    temp = n
    while temp > 0:
        rem = temp % 10
        sum = sum + pow(rem, count)
        temp = temp // 10

    if n == sum:
        return True
    else:
        return False


n = int(input())

res = check_Armstrong(n)
if res:
    print('true')
else:
    print('false')