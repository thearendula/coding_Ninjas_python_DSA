n = int(input())

even = 0
odd = 0

while n > 0:

    temp = n % 10
    if temp % 2 == 0:
        even = even + temp
    else:
        odd = odd + temp

    n = n // 10

print(even, " ", odd)
