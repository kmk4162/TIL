import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

graph = []
for i in range(5):
    line = list(map(str, input().split()))
    graph.append(line)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = []
def dfs(x, y, answer):
    if len(answer) == 6:
        if answer not in result:
            result.append(answer)
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if -1 < nx < 5 and -1 < ny < 5:
            dfs(nx, ny, answer + graph[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])
print(len(result))