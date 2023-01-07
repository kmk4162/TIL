import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
graph = []
for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

# 0 좌표 찾기
zero_list = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            zero_list.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def wall(arr):
    # 벽 세우기
    x1, y1 = arr[0][0], arr[0][1]
    x2, y2 = arr[1][0], arr[1][1]
    x3, y3 = arr[2][0], arr[2][1]
    graph[x1][y1] = 1
    graph[x2][y2] = 1
    graph[x3][y3] = 1

def bfs(row, col):
    queue = deque()
    queue.append((row, col))
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if -1 < nx < N and -1 < ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))

def zero_check():
    global cnt
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

answer = 0
for case in combinations(zero_list, 3):
    original = copy.deepcopy(graph)
    wall(case)
     # bfs 실행
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                bfs(i, j)
    cnt = 0
    new_cnt = zero_check()
    if new_cnt > answer:
        answer = new_cnt
    graph = original
print(answer)