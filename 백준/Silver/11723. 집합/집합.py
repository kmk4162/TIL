import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    line = list(input().split())
    cmd = line[0]
    if len(line) == 2:
        num = int(line[1])
    # print(cmd, num)

    if cmd == 'add':
        if num not in arr:
            arr.append(num)
    elif cmd == 'remove':
        if num in arr:
            arr.remove(num)
    elif cmd == 'check':
        if num in arr:
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        if num in arr:
            arr.remove(num)
        else:
            arr.append(num)
    elif cmd == 'all':
        arr = list(range(1, 21))
    else:
        arr = []