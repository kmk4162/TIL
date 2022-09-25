import sys
from collections import deque
input = sys.stdin.readline

# 그래프 입력 받기
M, N = map(int, input().split())
graph = []
for i in range(N):
    line = list(input().rstrip())
    graph.append(line)

# 아군은 W, 적군은 B, 몇 덩이 있는지 체크
# BFS 활용하자

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 전체 넓이 변수 저장
countW = 0
countB = 0

def findW(row, col):
    # 초기 설정
    queue = deque()
    queue.append((row, col))
    graph[row][col] = '1'
    cnt = 1
    while queue:
        row, col = queue.popleft()
        for d in range(4):
            nrow = row + dx[d]
            ncol = col + dy[d]
            if -1 < nrow < N and -1 < ncol < M and graph[nrow][ncol] == 'W':
                graph[nrow][ncol] = '1'
                cnt += 1
                queue.append((nrow, ncol))
    return cnt

def findB(row, col):
    # 초기 설정
    queue = deque()
    queue.append((row, col))
    graph[row][col] = '1'
    cnt = 1
    while queue:
        row, col = queue.popleft()
        for d in range(4):
            nrow = row + dx[d]
            ncol = col + dy[d]
            if -1 < nrow < N and -1 < ncol < M and graph[nrow][ncol] == 'B':
                graph[nrow][ncol] = '1'
                cnt += 1
                queue.append((nrow, ncol))
    return cnt

for x in range(N):
    for y in range(M):
        cnt = 0
        if graph[x][y] == 'W':
            answer = findW(x, y)
            countW += (answer ** 2)

        elif graph[x][y] == 'B':
            answer = findB(x, y)
            countB += (answer ** 2)
        
print(countW, countB)