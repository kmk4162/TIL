import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

dx = [-1, -1, 0]
dy = [-1, 0, -1]
answer = 0
for i in range(N):
    for j in range(M):
        now_max = 0
        for d in range(3):
            new_i = i + dx[d]
            new_j = j + dy[d]
            if -1 < new_i < N and -1 < new_j < M:
                if graph[new_i][new_j] > now_max:
                    now_max = graph[new_i][new_j]
        graph[i][j] += now_max
print(graph[N - 1][M - 1])