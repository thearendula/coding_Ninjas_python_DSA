def findUnique(arr):    length = len(arr)    for i in range(length):        j = 0        while j < length:            if i != j:                if arr[i] == arr[j]:                    break            j += 1        if j == length:            return arr[i]arr = [int(x) for x in input().split()]res = findUnique(arr)print(res)