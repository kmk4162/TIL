import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
graph = []
for _ in range(N):
    line = list(input().strip())
    graph.append(line)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * N for _ in range(N)]

# RGB 각각 체크하는 함수 만들기
def check_red(x, y):
    visited[x][y] = True
    for d in range(4):
        new_x = x + dx[d]
        new_y = y + dy[d]
        if -1 < new_x < N and -1 < new_y < N and visited[new_x][new_y] == False:
            if graph[new_x][new_y] == 'R':
                check_red(new_x, new_y)
def check_blue(x, y):
    visited[x][y] = True
    for d in range(4):
        new_x = x + dx[d]
        new_y = y + dy[d]
        if -1 < new_x < N and -1 < new_y < N and visited[new_x][new_y] == False:
            if graph[new_x][new_y] == 'B':
                check_blue(new_x, new_y)
def check_green(x, y):
    visited[x][y] = True
    for d in range(4):
        new_x = x + dx[d]
        new_y = y + dy[d]
        if -1 < new_x < N and -1 < new_y < N and visited[new_x][new_y] == False:
            if graph[new_x][new_y] == 'G':
                check_green(new_x, new_y)

def check_red_and_green(x, y): # 적녹색약만의 함수
    visited[x][y] = True
    for d in range(4):
        new_x = x + dx[d]
        new_y = y + dy[d]
        if -1 < new_x < N and -1 < new_y < N and visited[new_x][new_y] == False:
            if graph[new_x][new_y] != 'B' :
                check_red_and_green(new_x, new_y)

# 정상 경우 체크
normal_cnt = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R' and not visited[i][j]:
            check_red(i, j)
            normal_cnt += 1
        elif graph[i][j] == 'G' and not visited[i][j]:
            check_green(i, j)
            normal_cnt += 1
        elif graph[i][j] == 'B' and not visited[i][j]:
            check_blue(i, j)
            normal_cnt += 1

# visited 초기화
visited = [[False] * N for _ in range(N)]
abnormal_cnt = 0
for i in range(N):
    for j in range(N):
        if (graph[i][j] == 'R' or graph[i][j] == 'G') and not visited[i][j]:
            check_red_and_green(i, j)
            abnormal_cnt += 1
        elif graph[i][j] == 'B' and not visited[i][j]:
            check_blue(i, j)
            abnormal_cnt += 1
print(normal_cnt, abnormal_cnt)