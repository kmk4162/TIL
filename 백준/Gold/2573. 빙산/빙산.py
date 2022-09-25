import sys
input = sys.stdin.readline
from collections import deque

# 입력받기
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방문 처리, 매번 덩어리 셀 때마다 초기화해줘야함
visited = [[False] * M for _ in range(N)]

# 덩어리 개수 세는 BFS함수
# 좌표값이 0이 아닐때만 실행 시키기
def counter(row, col):
    visited[row][col] = True
    queue = deque()
    queue.append((row, col))
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            newx = x + dx[d]
            newy = y + dy[d]
            if -1 < newx < N and -1 < newy < M and visited[newx][newy] == False and graph[newx][newy] != 0:
                visited[newx][newy] = True
                queue.append((newx, newy))

# 빙산이 녹은 후를 보여주는 함수
def iceberg():
    # 일단 각 좌표별로 주위의 0이 몇개인지 세고 그걸 그대로 차집합 연산
    count_around_zero = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                cnt_zero = 0
                # 4면의 0개수 세기
                for d in range(4):
                    newi = i + dx[d]
                    newj = j + dy[d]
                    if graph[newi][newj] == 0:
                        cnt_zero += 1
                count_around_zero[i][j] = cnt_zero

    # 0 개수만큼 빼기 처리 하기, 0보다 작아지면 0으로 바꿔주기
    for i in range(N):
        for j in range(M):
            graph[i][j] -= count_around_zero[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

cnt_year = 0
while True:
    # 어차피 처음은 무조건 한 덩어리를 주기 때문에 1년이 지난 후부터 카운트하기
    cnt_year += 1
    iceberg()
    # pprint(f'{cnt_year}년 후')
    # pprint(graph)

    visited = [[False] * M for _ in range(N)]
    # 모든 좌표 돌면서 0이 아닐때만 덩어리 세기
    cnt_iceberg = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and visited[i][j] == False:
                counter(i, j)
                cnt_iceberg += 1

    if cnt_iceberg >= 2:
        break
    if cnt_iceberg == 0:
        cnt_year = 0
        break

print(cnt_year)