import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    if x == target_x and y == target_y:
        return False
    while queue:
        x, y = queue.popleft()
        for d in range(8):
            new_x = x + dx[d]
            new_y = y + dy[d]
            if -1 < new_x < N and -1 < new_y < N:
                if not graph[new_x][new_y]:
                    graph[new_x][new_y] = graph[x][y] + 1
                    queue.append((new_x, new_y))
    return True

for case in range(T):
    N = int(input().strip())
    graph = [[0] * N for _ in range(N)]
    now_x, now_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    if not bfs(now_x, now_y):
        print(0)
    else:
        print(graph[target_x][target_y])