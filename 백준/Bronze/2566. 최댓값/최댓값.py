import sys
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(9)]
row = 0
col = 0
answer = 0
for i in range(9):
    for j in range(9):
        if graph[i][j] > answer:
            row = i
            col = j
            answer = graph[i][j]
print(answer)
print(row + 1, col + 1)