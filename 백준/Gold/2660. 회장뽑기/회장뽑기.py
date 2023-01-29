import sys
input = sys.stdin.readline

N = int(input())
INF = int(10e4)
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

while True:
    a, b = map(int, input().split())
    if (a, b) == (-1, -1):
        break
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = []
for i in range(1, N + 1):
    cnt = 0
    for j in range(1, N + 1):
        if graph[i][j] > cnt:
            cnt = graph[i][j]
    answer.append(cnt)

score = min(answer)
people = answer.count(score)
print(score, people)
for i in range(len(answer)):
    if answer[i] == score:
        print(i + 1, end = ' ')