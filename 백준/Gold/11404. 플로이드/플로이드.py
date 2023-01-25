import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(10e6)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    answer = []
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            answer.append(0)
        else:
            answer.append(graph[i][j])
    print(*answer)