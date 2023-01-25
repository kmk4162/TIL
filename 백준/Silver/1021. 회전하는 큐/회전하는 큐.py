import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = list(map(int, input().split()))

queue = deque()
for i in range(1, N + 1):
    queue.append(i)

cnt = 0
queue_length = N
for j in arr:
    while True:
        if queue[0] == j:
            queue.popleft()
            break
        else:
            if queue.index(j) < len(queue) / 2:
                while queue[0] != j:
                    queue.append(queue.popleft())
                    cnt += 1
            else:
                while queue[0] != j:
                    queue.appendleft(queue.pop())
                    cnt += 1

print(cnt)