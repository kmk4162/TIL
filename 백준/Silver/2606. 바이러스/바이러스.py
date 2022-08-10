# N은 컴퓨터 수, M은 간선 수
N = int(input())
M = int(input())

# 연결리스트 만들기
comlist = [[] for _ in range(N + 1)]
for i in range(M):
    v1, v2 = map(int, input().split())
    comlist[v1].append(v2)
    comlist[v2].append(v1)

visited = [False] * (N + 1)
# stack에는 돌아갈 곳을 기록하는 곳
stack = [1]
# 1에서 시작하니까 이미 방문한 것이므로 True로 바꿈
visited[1] = True

while True:
    # 처음에는 1을 pop함
    now = stack.pop()
    # 인덱스 1의 요소들을 순회하면서 
    # 처음 가본 곳이면 False 상태여서 True로 바꿔주고 stack에 추가
    # 만약 이미 가본 곳이면 True일 것이므로 조건 만족 안하므로 stack에 추가 안됨
    for adj in comlist[now]:
        if visited[adj] == False:
            visited[adj] = True
            stack.append(adj)
    # 이런식으로 반복하면서 한번도 안 가본곳이 존재하면 append 동작을 할텐데
    # 모든 인덱스가 다 방문했어서 True라면 append는 더이상 실행되지않고
    # stack은 결국 빈 리스트가 됨 이때 반복을 중지하면 됨!
    if stack == []:
        break
print(sum(visited) - 1)
