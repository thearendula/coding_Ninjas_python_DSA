def bubbleSort(arr, n):    for i in range(n - 1):        for j in range(n - i - 1):            if arr[j] > arr[j + 1]:                arr[j + 1], arr[j] = arr[j], arr[j + 1]n = int(input())arr = [int(x) for x in input().split()]bubbleSort(arr, n)print(arr)