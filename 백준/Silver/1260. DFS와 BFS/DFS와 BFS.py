N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# 연결 리스트 만들기
for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

# 문제 조건 맞추기위해 그래프를 오름차순으로 정렬
for i in graph:
    i.sort()

# 방문 표시
visited= [False] * (N + 1)

# dfs
def dfs(V):
    visited[V] = True
    print(V, end = ' ')
    for i in graph[V]:
        if not visited[i]:
            dfs(i)
dfs(V)

# bfs
from collections import deque

# 방문리스트 초기화
visited= [False] * (N + 1)

def bfs(V):
    queue = deque()
    queue.append(V)
    visited[V] = True
    while queue:
        i = queue.popleft()
        print(i, end = ' ')
        for x in graph[i]:
            if not visited[x]:
                queue.append(x)
                visited[x] = True
print()
bfs(V)