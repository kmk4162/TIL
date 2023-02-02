import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def bfs(row, col):
    q = deque()
    q.append((row, col))
    graph[row][col] = 0
    while q:
        x, y = q.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if -1 < nx < N and -1 < ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))

cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            bfs(i, j)
            cnt += 1
print(cnt)