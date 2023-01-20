import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
arr = list(map(int, input().split()))
answer = deque()
answer.append(N)
for i in range(N - 1, 0, -1):
    if len(answer) == arr[i - 1]:
        answer.append(i)
    else:
        answer.insert(arr[i - 1], i)
print(*list(answer))