import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
graph = []
for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

def chicken_check():# 치킨집 좌표 찾기
    arr = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                arr.append((i, j))
    return arr
    
def home_check(): # 집 몇개 있는지
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                cnt += 1
    return cnt

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def distance(row, col, arr): # 좌표가 1(집)일때 실행
    min_dis = 10e9
    for i in arr:
        now_dis = abs(i[0] - row) + abs(i[1] - col)
        if now_dis < min_dis:
            min_dis = now_dis
    return min_dis

chicken_list = chicken_check()

if len(chicken_list) <= M:
    answer = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                answer += distance(i, j, chicken_list)
else:
    answer = 10e9
    for case in combinations(chicken_list, M):
        cnt = 0
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 1:
                    cnt += distance(i, j, case)
        if cnt < answer:
            answer = cnt
print(answer)