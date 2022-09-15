import sys
input = sys.stdin.readline

# N이 정점 개수, M이 간선 개수
N, M = map(int, input().split())

# 0 인덱스는 사용 안 하니까 N + 1만큼의 빈 리스트 만들기
graph = [[] for _ in range(N + 1)]

# 간선 추가하기
for i in range(M):
    a, b = map(int, input().split())
    # 무방향이니까 2번씩 추가하기
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
stack = [1]
# 0번은 실제로 없으니까 애초부터 True로 고정
visited[0] = True
# 1은 시작점이니까 True
visited[1] = True
cnt = 0
while True:
    start = stack.pop()
    # 해당 정점에 인접하는 요소가 1개라도 있을때만 고려
    if len(graph[start]) != 0:
        for i in graph[start]:
            if visited[i] == False:
                visited[i] = True
                stack.append(i)   
    # 정점에 아무것도 존재하지 않으면 자기자신만 있는 것이므로, 자기자신 카운트 1개만 한다고 생각, 바로 True로 바꿔주기
    else:
        visited[start] = True    
    # 반복이 다 끝나면 카운트 올리고 나머지 돌게 해줌
    if stack == []:
        cnt += 1
        # visited에 아직 False가 있다면 반복 계속
        if False in visited:
            # 아직 False인 애들 중에 하나를 stack에 넣어줘야함
            # False가 있는 인덱스를 visited 리스트에서 찾아서 stack에 추가
            stack = [visited.index(False)]
            continue
        else:
            break
print(cnt)