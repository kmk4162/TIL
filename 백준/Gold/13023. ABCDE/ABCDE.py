import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] * N for _ in range(N)]
visited = [False] * N
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 깊이가 5면 만족?
def dfs(idx, number):
    if number == 4:
        print(1)
        exit()
    for i in graph[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, number + 1)
            visited[i] = False

for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)