import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
graph = []
for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

# 처음 실행
def check():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return False
    return True

def tomato_check():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] > cnt:
                cnt = graph[i][j]
    return cnt

if check():
    print(0)
else:
    bfs()
    if check():
        print(tomato_check() - 1)
    else:
        print(-1)