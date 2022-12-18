import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

row_sum_graph = []
for i in range(N):
    line = []
    sum_number = 0
    for j in range(N):
        sum_number += graph[i][j]
        line.append(sum_number)
    row_sum_graph.append(line)

for case in range(M):
    answer = 0
    x1, y1, x2, y2 = map(int, input().split())
    for row in range(x1, x2 + 1):
        if y1 != 1:
            answer += (row_sum_graph[row-1][y2-1] - row_sum_graph[row-1][y1-2])
        else:
            answer += row_sum_graph[row-1][y2-1]
    print(answer)