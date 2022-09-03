from collections import deque
from pprint import pprint
# 0은 배추가 심어져 있지 않은 땅
# 1은 배추가 있는 부분들
# -> 1로 연결돼있는 연결 요소의 개수를 구하는 것

T = int(input())
for i in range(T):
    # 가로, 세로, 배추의 개수
    M, N, Y = map(int, input().split())

    # 기초 그래프 만들기
    graph = [[0] * N for _ in range(M)]

    # 배추 위치 업데이트    
    for k in range(Y):
        row, col = map(int, input().split())
        graph[row][col] = 1

    # 델타 리스트 만들기
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    cnt = 0
    # BFS 함수
    def BFS(x, y):
        queue = deque([])
        queue.append((x,y))
        graph[x][y] == 0
        while queue:
            x, y = queue.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if -1 < nx < M and -1 < ny < N and graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
    for x in range(M):
        for y in range(N):
            if graph[x][y] == 1:
                BFS(x,y)
                cnt += 1
    print(cnt)