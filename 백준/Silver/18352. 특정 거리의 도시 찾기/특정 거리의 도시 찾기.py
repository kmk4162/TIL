import sys
input = sys.stdin.readline
from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
visited = [False for _ in range(N + 1)]
distance = [0 for _ in range(N + 1)]
visited[0] = True
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    distance[start] = 0
    while queue:
        # 시작점에서 아예 간선이 없으면 바로 종료
        if not graph[start]:
            break
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                distance[i] = distance[x] + 1
        if distance[i] > K:
            break

bfs(X)
is_exist = False
for i in range(len(distance)):
    if distance[i] == K:
        print(i)
        is_exist = True
if not is_exist:
    print(-1)