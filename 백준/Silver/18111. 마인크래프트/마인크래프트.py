import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
graph = []
for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)

max_graph = max(map(max, graph))
min_graph = min(map(min, graph))
answer_height = 0
answer_time = 1e9
for height in range(min_graph, max_graph + 1):
    max_cnt = 0
    min_cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] > height:
                max_cnt += (graph[i][j] - height)
            else:
                min_cnt += (height - graph[i][j])
    inventory = max_cnt + B # 인벤토리에 있는 총 블록 수
    if inventory < min_cnt: # 제거하는게 더 많으면 불가능
        continue
    time = 2 * max_cnt + min_cnt
    if time <= answer_time:
        answer_time = time
        answer_height = height
print(answer_time, answer_height)