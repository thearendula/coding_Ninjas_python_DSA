def swapAlternate(arr, n):    if n % 2 == 0:        for i in range(0, n, 2):            arr[i], arr[i + 1] = arr[i + 1], arr[i]            return arr    else:        for i in range(0, n - 1, 2):            arr[i], arr[i + 1] = arr[i + 1], arr[i]        return arrn = int(input())arr = [int(x) for x in input().split()]swapAlternate(arr, n)print(arr)