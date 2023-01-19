import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    line = list(map(int, input().strip()))
    graph.append(line)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * M for _ in range(N)]
def bfs(row, col):
    visited[row][col] = True
    queue = deque()
    queue.append((row, col))
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if -1 < nx < N and -1 < ny < M and not visited[nx][ny] and graph[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = True

for j in range(M):
    if graph[0][j] == 0:
        bfs(0, j)

flag = False
for j in range(M):
    if visited[N - 1][j] == True:
        flag = True
        break
if flag:
    print('YES')
else:
    print('NO')