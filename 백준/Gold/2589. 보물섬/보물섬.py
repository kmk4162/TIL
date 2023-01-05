import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    line = list(input().strip())
    graph.append(line)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(row, col):
    queue = deque()
    queue.append((row, col))
    visited = [[-1] * M for _ in range(N)]
    visited[row][col] = 0
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            new_x = x + dx[d]
            new_y = y + dy[d]
            if -1 < new_x < N and -1 < new_y < M and graph[new_x][new_y] == 'L' and visited[new_x][new_y] == -1:
                visited[new_x][new_y] = visited[x][y] + 1
                queue.append((new_x, new_y))
                # pprint(visited)
                # print(new_x, new_y)
    return visited[x][y]

answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            cnt = bfs(i, j)
            if cnt > answer:
                answer = cnt
print(answer)