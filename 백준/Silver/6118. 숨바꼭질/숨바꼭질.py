import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1 for _ in range(N + 1)]
def bfs(): # 시작은 1
    visited[1] = 0
    queue = deque()
    queue.append(1)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == -1:
                visited[i] = visited[x] + 1
                queue.append(i)
bfs()
max_arr = max(visited)
answer = []
for i in range(len(visited)):
    if visited[i] == max_arr:
        answer.append(i)
print(min(answer), max_arr, len(answer))