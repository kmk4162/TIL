import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
# 공기청정기 좌표 찾기
for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            air_high = [i, j]
            air_low = [i + 1, j]
# break가 안 먹혀서 좌표값 -1 강제로
air_high[0] -= 1
air_low[0] -= 1
# print(air_high, air_low)

def diffusion(graph):
    # 1초 사이에 미세먼지가 어떻게 변하는지 증감을 적는 그래프
    graph_change_diff = [[0] * C for _ in range(R)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for x in range(R):
        for y in range(C):
            #  공기청정기가 있으면 그냥 패스
            if graph[x][y] == -1:
                continue
            # 확산이 몇개의 방향으로 되는지
            cnt_diff = 0
            # 동서남북 카운트하기
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                # 확산 가능 한 방향일때만 카운트 +1     
                if -1 < nx < R and -1 < ny < C and graph[nx][ny] != -1:
                    graph_change_diff[nx][ny] += graph[x][y] // 5
                    cnt_diff += 1
            graph_change_diff[x][y] -= (graph[x][y] // 5) * cnt_diff
    # 그래프에 변화 반영하기
    for i in range(R):
        for j in range(C):
            graph[i][j] += graph_change_diff[i][j]
    # pprint(graph)
    # print('-------------------')

def air(graph):
     # 1초 사이에 공기청정기에 의해 어떻게 변하는지 적는 그래프
    graph_change_air = [[0] * C for _ in range(R)]
        
    # 위쪽 공기청정기 순환
    # 1. 윗변
    for j in range(1, C):
        graph_change_air[0][j] -= graph[0][j]
        graph_change_air[0][j - 1] += graph[0][j]
    # 2. 왼쪽변
    for i in range(0, air_high[0]):
        if i != air_high[0] -1:
            graph_change_air[i][0] -= graph[i][0]
            graph_change_air[i + 1][0] += graph[i][0]
        else:
            graph_change_air[i][0] -= graph[i][0]
    # 3. 밑변
    for j in range(1, C - 1):
        graph_change_air[air_high[0]][j] -= graph[air_high[0]][j]       
        graph_change_air[air_high[0]][j + 1] += graph[air_high[0]][j]
    # 4. 오른쪽변
    for i in range(1, air_high[0] + 1):
        graph_change_air[i][C - 1] -= graph[i][C - 1]
        graph_change_air[i - 1][C - 1] += graph[i][C - 1]
    # pprint(graph_change_air)
    # print('-------------------')

    # 아래쪽 공기청정기 순환
    # 1. 윗변
    for j in range(1, C - 1):
        graph_change_air[air_low[0]][j] -= graph[air_low[0]][j]
        graph_change_air[air_low[0]][j + 1] += graph[air_low[0]][j]
    # 2. 오른쪽변
    for i in range(air_low[0], R - 1):
        graph_change_air[i][C - 1] -= graph[i][C - 1]
        graph_change_air[i + 1][C - 1] += graph[i][C - 1]
    # 3. 밑변
    for j in range(1, C):
        graph_change_air[R - 1][j] -= graph[R - 1][j]       
        graph_change_air[R - 1][j - 1] += graph[R - 1][j]
    # 4. 왼쪽변
    for i in range(air_low[0] + 1, R):
        if i != air_low[0] + 1:
            graph_change_air[i][0] -= graph[i][0]
            graph_change_air[i - 1][0] += graph[i][0]
        else:
            graph_change_air[i][0] -= graph[i][0]
    # 변화 반영
    for i in range(R):
        for j in range(C):
            graph[i][j] += graph_change_air[i][j]

 # time 만큼 반복
for i in range(T):
    # print(i + 1,'초')
    diffusion(graph)
    # pprint(graph)
    # print('-------------------')
    air(graph)
    # pprint(graph)
    # print('-------------------')

# 전체 값 더하기
answer = 0
for i in range(R):
    for j in range(C):
        answer += graph[i][j]
# 공기 청정기 -1 2개는 무효처리
answer += 2
print(answer)