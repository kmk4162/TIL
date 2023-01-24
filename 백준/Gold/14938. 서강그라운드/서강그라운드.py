import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
INF = int(10e6)
graph = [[INF] * (N + 1) for _ in range(N + 1)]
arr = list(map(int, input().split()))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(R):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
   

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])

answer = max(arr)
for i in range(1, N + 1):
    score = arr[i - 1]
    for j in range(1, N + 1):
        if graph[i][j] <= M and i != j:
            score += arr[j - 1]
    if score > answer:
        answer = score
# pprint(graph)
print(answer)