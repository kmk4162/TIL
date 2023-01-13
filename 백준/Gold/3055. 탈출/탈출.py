import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
graph = []
for i in range(R):
    line = list(input().strip())
    graph.append(line)

# 물 있는 곳은 0, 시간 지날수록 1씩 증가
INF = int(10e9)
ground = [[INF] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if graph[i][j] == '*':
            ground[i][j] = 0
# pprint(ground)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def water(x, y):
    queue= deque()
    water = [[False] * C for _ in range(R)]
    water[x][y] = True
    queue.append((x, y))
    while queue:
        i, j = queue.popleft()
        for d in range(4):
            ni = i + dx[d]
            nj = j + dy[d]
            if -1 < ni < R and -1 < nj < C and not graph[ni][nj] == 'X' and not graph[ni][nj] == 'D':
                if not water[ni][nj]:
                    ground[ni][nj] = min(ground[ni][nj], ground[i][j] + 1)
                    queue.append((ni, nj))
                    water[ni][nj] = True

def move(x, y, c):
    queue = deque()
    visited = [[False] * C for _ in range(R)]
    visited[x][y] = True
    queue.append((x, y, c))
    while queue:
        i, j, cnt = queue.popleft()
        for d in range(4):
            ni = i + dx[d]
            nj = j + dy[d]
            if -1 < ni < R and -1 < nj < C:
                if ni == home[0] and nj == home[1]:
                    visited[home[0]][home[1]] = True
                    return cnt + 1
                if graph[ni][nj] == 'X':
                    continue
                if ground[ni][nj]- 1 > cnt and not visited[ni][nj]:
                    queue.append((ni, nj, cnt + 1))
                    visited[ni][nj] = True
    # 굴에 도달 못한 경우
    if not visited[home[0]][home[1]]:
        return 'KAKTUS'

for i in range(R):
    for j in range(C):
        if ground[i][j] == 0:
            water(i, j)
        if graph[i][j] == 'D':
            home = (i, j)
        if graph[i][j] == 'S':
            start = (i, j)
print(move(start[0], start[1], 0))