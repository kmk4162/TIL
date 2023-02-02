import sys
input = sys.stdin.readline

N = int(input())
INF = int(10e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    arr = list(input().strip())
    for j in range(N):
        if arr[j] == 'Y':
            graph[i][j + 1] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

answer = 0
for i in range(1, N + 1):
    cnt = 0
    for j in range(1, N + 1):
        if 1 <= graph[i][j] <= 2:
            cnt += 1
    if cnt > answer:
        answer = cnt

print(answer)