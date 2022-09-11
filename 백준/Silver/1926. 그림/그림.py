from collections import deque
from pprint import pprint

N, M = map(int, input().split())
graph = []
cnt = 0
cnt_area = 0
list_area = []

for i in range(N):
    j = list(map(int, input().split()))
    graph.append(j)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(row, col, cnt_area):
    cnt_area += 1
    queue = deque()
    queue.append((row, col))
    graph[row][col] = 0
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if -1 < nx < N and -1 < ny < M and graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = 0
                cnt_area += 1
    list_area.append(cnt_area)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            cnt += 1
            BFS(i, j, 0)
print(cnt)
if not list_area:
    print(0)
else:
    print(max(list_area))