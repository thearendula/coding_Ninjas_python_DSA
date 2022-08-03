def printTable(start, end, step):
    for i in range(start, end+1, step):
        cel = int((i - 32) * 5/9)
        print(i, cel)


s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)