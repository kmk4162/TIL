import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(row, col):
    queue = deque()
    queue.append((row, col))
    visited[row][col] = True
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if -1 < nx < H and -1 < ny < W and not visited[nx][ny] and graph[nx][ny] == '#':
                visited[nx][ny] = True
                queue.append((nx, ny))

for i in range(T):
    H, W = map(int, input().split())
    graph = []
    for i in range(H):
        line = list(input().strip())
        graph.append(line)
    
    cnt = 0
    visited = [[False] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if graph[i][j] == '#' and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)