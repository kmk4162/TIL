import sys
input = sys.stdin.readline
from copy import deepcopy

N = int(input())

max_prev = [0, 0, 0]
min_prev = [0, 0, 0]
max_now = [0, 0, 0]
min_now = [0, 0, 0]
for i in range(N):
    line = list(map(int, input().split()))

    max_now[0] = max(max_prev[0], max_prev[1]) + line[0] 
    min_now[0] = min(min_prev[0], min_prev[1]) + line[0]
    max_now[1] = max(max_prev[0], max_prev[1], max_prev[2]) + line[1]
    min_now[1] = min(min_prev[0], min_prev[1], min_prev[2]) + line[1]
    max_now[2] = max(max_prev[1], max_prev[2]) + line[2]
    min_now[2] = min(min_prev[1], min_prev[2]) + line[2]

    max_prev = deepcopy(max_now)
    min_prev = deepcopy(min_now)
print(max(max_now), min(min_now)) 