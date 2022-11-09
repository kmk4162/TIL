import sys
input = sys.stdin.readline
from itertools import *

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# 한 팀의 명수는 N / 2
# N = 4, 경우의 수는 12 13 14
# N = 6, 경우의 수는 123 124 125 126 134 135 136 145 146 156
for i in range(N):
    for j in range(N):
        if i < j:
            graph[j][i] += graph[i][j]
            graph[i][j] = 0
# pprint(graph)
# 0 0 0 0
# 5 0 0 0
# 9 6 0 0
# 6 10 7 0
nlist = list(range(1, N + 1))
cases = []
for case in combinations(nlist, int(N / 2)):
    if case[0] == 1:
        cases.append(case)

result = []
for i in cases:
    score = 0
    opposite_score = 0
    opposites = sorted(set(range(1, N + 1)) - set(i))
    
    # 경우의 수 안에서 2개씩 뽑는 경우를 다 구함
    for case1 in combinations(i, 2):
        score += graph[case1[1] - 1][case1[0] - 1]
    for case2 in combinations(opposites, 2):
        opposite_score += graph[case2[1] - 1][case2[0] - 1]
    real_score = abs(score - opposite_score)
    result.append(real_score)
    # print(real_score, '|', i, opposites)
print(min(result))