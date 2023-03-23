import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    line = list(map(int, input().strip()))
    graph.append(line)

# [벽 안 뚫은 경우 거리, 벽 뚫은 경우 거리]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    queue = deque()
    queue.append((0, 0, 0)) # 기본 좌표에다가 벽 부쉈는지 아닌지 정보 추가
    visited[0][0][0] = 1 # 초기 거리 1

    while queue:
        x, y, b = queue.popleft()
        if x == N - 1 and y == M - 1: # 맨 끝 도달하면 리턴
            return visited[x][y][b]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if - 1 < nx < N and -1 < ny < M:
                if graph[nx][ny] == 0 and visited[nx][ny][b] == 0:
                    visited[nx][ny][b] = visited[x][y][b] + 1
                    queue.append((nx, ny, b))
                elif graph[nx][ny] == 1 and b == 0:
                    visited[nx][ny][b + 1] = visited[x][y][b] + 1
                    queue.append((nx, ny, b + 1))
    return -1    
print(bfs())