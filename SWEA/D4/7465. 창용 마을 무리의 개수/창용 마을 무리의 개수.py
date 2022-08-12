T = int(input())
# DFS 함수 만들기
def DFS(start):
    stack = [start]
    visited[start] = True
    while len(stack) != 0:
        cur = stack.pop()
        for adj in people[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
    return

for test_case in range(1, T + 1):
    # 간선, 정점 입력받고 인접리스트 만들기
    N, M = map(int, input().split())
    people = [[] for _ in range(N + 1)]
    for i in range(M):
        v1, v2 = map(int, input().split())
        people[v1].append(v2)
        people[v2].append(v1)
    # DFS 돌리기
    visited = [False] * (N + 1)
    visited[0] = True
    cnt = 1
    DFS(1)
    while False in visited:
        next_index = (visited.index(False))
        cnt += 1
        DFS(next_index)
    print(f'#{test_case} {cnt}') 