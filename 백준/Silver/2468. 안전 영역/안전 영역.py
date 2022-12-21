import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = []
for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

def height_check(h):
    for i in range(N):
        for j in range(N):
            if graph[i][j] <= h:
                check[i][j] = False

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y):
    global check
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            new_x = x + dx[d]
            new_y = y + dy[d]
            if -1 < new_x < N and -1 < new_y < N and check[new_x][new_y] and not visited[new_x][new_y]:
                queue.append((new_x, new_y))
                visited[new_x][new_y] = True

# graph의 최댓값 구하기 -> 최대 높이까지만 구하기
max_height = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] > max_height:
            max_height = graph[i][j]

answer = 0
for height in range(0, max_height + 1):
    cnt = 0
    check = [[True] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    height_check(height)
    for i in range(N):
        for j in range(N):
            if check[i][j] and not visited[i][j]:
                cnt += 1
                bfs(i, j)
    if cnt > answer:
        answer = cnt
print(answer)