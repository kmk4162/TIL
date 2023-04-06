import sys
input = sys.stdin.readline
from collections import deque

graph = []
for _ in range(12):
    line = list(input().strip())
    graph.append(line)

# 4개 이상 연결 돼있으면 .으로 바꾸기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(row, col, mark):
    global flag
    queue = deque()
    queue.append((row, col))
    visited[row][col] = True
    cnt = 1
    arr = []
    while queue:
        x, y = queue.popleft()
        arr.append((x, y)) # 같은 글자 좌표를 arr에 넣기
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if -1 < nx < 12 and -1 < ny < 6 and not visited[nx][ny] and graph[nx][ny] == mark:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1
    # 4이상이면 arr에 있는 좌표쌍들을 다 .으로 바꾸기
    if cnt >= 4:
        for i in arr:
            graph[i[0]][i[1]] = '.'
        flag = True      
    return flag

        

# 다 터뜨린 다음에 시행
def down():
    for i in range(6): # 세로 기준
        queue = deque()
        for j in range(11, -1, -1): # 거꾸로 생각
            if graph[j][i] != '.':
                queue.append(graph[j][i])

        for j in range(11, -1, -1):
            if queue:
                graph[j][i] = queue.popleft()
            else:
                graph[j][i] = '.'


answer = 0
while True:
    visited = [[False] * 6 for _ in range(12)]
    flag = False
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and not visited[i][j]:
                bfs(i, j, graph[i][j])
    down()
    if not flag:
        break
    else:
        answer += 1
print(answer)