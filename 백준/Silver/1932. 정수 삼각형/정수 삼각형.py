import sys
input = sys.stdin.readline

N = int(input())
graph = []
for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

if N == 1:
    print(graph[0][0])
elif N == 2:
    print(max(graph[1][0], graph[1][1]) + graph[0][0])
else:
    graph[1][0] = graph[0][0] + graph[1][0]
    graph[1][1] = graph[0][0] + graph[1][1]
    for i in range(2, N):
        for j in range(i + 1):
            if j == 0:
                graph[i][j] = graph[i-1][j] + graph[i][j]
            elif j == i:
                graph[i][j] = graph[i-1][j-1] + graph[i][j]
            else:
                graph[i][j] = max(graph[i-1][j-1], graph[i-1][j]) + graph[i][j]
    print(max(graph[-1]))