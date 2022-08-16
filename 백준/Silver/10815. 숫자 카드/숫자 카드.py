N = int(input())
checkdict = {}
for num in list(map(int, input().split())):
    checkdict[num] = 1
M = int(input())
for check in list(map(int, input().split())):
    if check in checkdict:
        print(1, end = ' ')
    else:
        print(0, end = ' ')