import sys
input = sys.stdin.readline
sys.setrecursionlimit(2500)

def DFS(x, y, visited):
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if -1 < nx < height and -1 < ny < width and visited[nx][ny] == False and graph[nx][ny] == 1:
            visited[nx][ny] = True
            DFS(nx, ny, visited)

while True:
    width, height = map(int, input().split())
    # 8방향
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    if width == 0 and height == 0:
        break
    else:
        graph = []
        for i in range(height):
            line = list(map(int, input().split()))
            graph.append(line)
        visited = [[False] * width for _ in range(height)]
        cnt = 0
        for i in range(height):
            for j in range(width):
                if graph[i][j] == 1 and visited[i][j] == False:
                    visited[i][j] = True
                    DFS(i, j, visited)
                    cnt += 1
        print(cnt)