import sys
input = sys.stdin.readline
from collections import deque

M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]

def check(y1, x1, y2, x2):
    global graph
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = -1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(row, col, graph, block):
    queue = deque()
    queue.append((row, col))
    graph[row][col] = 1
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if -1 < nx < M and -1 < ny < N and graph[nx][ny] == 0:
                graph[nx][ny] = -1
                queue.append((nx, ny))
                block += 1   
    return block

for i in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    check(y1, x1, y2, x2)

cnt = 0
answer = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            answer.append(bfs(i, j, graph, 1))
            cnt += 1
print(cnt)
print(*(sorted(answer)))