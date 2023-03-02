import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    line = list(input().strip())
    graph.append(line)
visited = [[False] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check(row, col):
    global sheep, wolf
    if graph[row][col] == 'v':
        wolf += 1
    elif graph[row][col] == 'o':
        sheep += 1
    queue = deque()
    queue.append((row, col))
    visited[row][col] = True
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if -1 < nx < N and -1 < ny < M and not visited[nx][ny] and graph[nx][ny] != '#':
                if graph[nx][ny] == 'v':
                    wolf += 1
                elif graph[nx][ny] == 'o':
                    sheep += 1
                visited[nx][ny] = True
                queue.append((nx, ny))

    if sheep > wolf:
        wolf = 0
    else:
        sheep = 0
    return (sheep, wolf)

wolf_cnt = 0
sheep_cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] != '#' and not visited[i][j]:
            sheep = 0
            wolf = 0
            answer = check(i, j)
            sheep_cnt += answer[0]
            wolf_cnt += answer[1]

print(sheep_cnt, wolf_cnt)