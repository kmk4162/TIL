import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(M):
    line = list(map(int, input().strip()))
    graph.append(line)
dist = [[-1] * N for _ in range(M)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(row, col):
    queue = deque()
    queue.append((row, col))
    dist[row][col] = 0
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if -1 < nx < M and -1 < ny < N:
                if dist[nx][ny] == -1:
                    if graph[nx][ny] == 0:
                       dist[nx][ny] = dist[x][y]
                       queue.appendleft((nx, ny))
                    else:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))
                        
bfs(0, 0)
print(dist[M - 1][N - 1])
