import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    line = list(map(int, input().strip()))
    graph.append(line)

# DFS
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * N for _ in range(N)]


def DFS(graph, x, y):
    global cnt
    for d in range(4):
        new_x = x + dx[d]
        new_y = y + dy[d]
        if -1 < new_x < N and -1 < new_y < N and visited[new_x][new_y] == False and graph[new_x][new_y] != 0:
            visited[new_x][new_y] = True
            cnt += 1
            DFS(graph, new_x, new_y)

cnt_arr = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == False and graph[i][j] != 0:
            cnt = 1
            visited[i][j] = True
            DFS(graph, i, j)
            cnt_arr.append(cnt)
print(len(cnt_arr))
cnt_arr.sort()
for i in cnt_arr:
    print(i)