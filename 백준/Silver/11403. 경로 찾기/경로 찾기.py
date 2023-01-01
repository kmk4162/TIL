import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = []
for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

adj_list = [[] for _ in range(N + 1)] # 인접 리스트
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            adj_list[i + 1].append(j + 1)

def check(start, end):
    visited = [True] + [False] * (N)
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft()
        for i in adj_list[x]:
            if i == end:
                return True
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return False

for i in range(N):
    for j in range(N):
        if check(i + 1, j + 1):
            graph[i][j] = 1

for i in graph:
    print(*i)