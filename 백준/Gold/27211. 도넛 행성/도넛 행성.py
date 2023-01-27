import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * M for _ in range(N)]

def bfs(row, col):
    queue = deque()
    queue.append((row, col))
    visited[row][col] = True
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx == -1:
                nx = N - 1
            if nx == N:
                nx = 0
            if ny == -1:
                ny = M - 1
            if ny == M:
                ny = 0
            if not visited[nx][ny] and graph[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = True
                
cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not visited[i][j]:
            bfs(i, j)
            cnt += 1
print(cnt)