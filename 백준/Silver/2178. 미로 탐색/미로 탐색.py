import sys
input = sys.stdin.readline
from collections import deque

row, col = map(int, input().split())
graph = []
for i in range(row):
    line = list(map(int, input().strip()))
    graph.append(line)
# pprint(graph)

visited = [[False] * col for _ in range(row)]
# pprint(visited)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 초기값
visited[0][0] = True
def BFS(graph, x, y):
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if -1 < nx < row and -1 < ny < col and visited[nx][ny] == False and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    return graph[row - 1][col - 1]
print(BFS(graph, 0, 0))