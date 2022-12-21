import sys
input = sys.stdin.readline
from collections import deque

def bfs(graph, v):
    queue = deque()
    queue.append(v)
    # 처음 방문은 1, 그다음부터 -1씩 곱해서 번갈아 방문표시
    visited[v] = 1
    # 추가한 코드
    # 그룹을 나누어서 서로 인접 정점끼리 다른 그룹이어야함
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                # 지금 그룹이랑 다른 그룹을 넣어줌
                visited[i] = -1 * visited[x]
                queue.append(i)
            # 이미 방문했는데 동일한 그룹에 속하면 False
            # 이미 방문했는데 다른 그룹이라면 그냥 넘어감
            else:
                if visited[i] == visited[x]:
                    return False
    return True

T = int(input())
for case in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for i in range(E): # 간선 개수 만큼 입력 받기
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    
    answer = True
    visited = [0] * (V + 1)
    for v in range(1, V + 1):
        if visited[v] == 0:
            if not bfs(graph, v):
                answer = False
                break
    if answer:
        print('YES')
    else:
        print('NO')