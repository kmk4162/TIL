import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        x = queue.popleft()
        if not visited[graph[x]]:
            queue.append(graph[x])
            visited[graph[x]] = True

T = int(input())
for case in range(T):
    N = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False for _ in range(N + 1)]
    cnt = 0
    for i in range(1, N + 1):
        if not visited[i]:
            cnt += 1
            bfs(i)
    print(cnt)