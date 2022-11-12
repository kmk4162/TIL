import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = deque()

for i in range(N):
    word = input().split()
    # print(word)
    if 'push' in word:
        arr.append(int(word[-1]))
    elif word[0] == 'pop':
        if len(arr) != 0:
            x = arr.popleft()
            print(x)
        else:
            print(-1)
    elif word[0] == 'size':
        print(len(arr))
    elif word[0] == 'empty':
        if len(arr) != 0:
            print(0)
        else:
            print(1)
    elif word[0] == 'front':
        if len(arr) != 0:
            print(arr[0])
        else:
            print(-1)
    elif word[0] == 'back':
        if len(arr) != 0:
            print(arr[-1])
        else:
            print(-1)
    # print(arr)