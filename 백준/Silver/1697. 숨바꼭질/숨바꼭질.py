from collections import deque

N, K = map(int, input().split())

# 거리 저장 리스트
dist = [0] * 100001

def bfs():
    # 초기 설정
    queue = deque()
    queue.append(N)
    while queue:
        s = queue.popleft()
        if s == K:
            print(dist[s])
            break
        # -1, +1, *2를 탐색
        for ns in (s - 1, s + 1 , s * 2):
            if 0 <= ns <= 100000 and dist[ns] == 0:
                dist[ns] = dist[s] + 1
                queue.append(ns)
# N이 5였으면 첫 반복을 4, 6, 10을 돌고
# dist[4], dist[6], dist[10]은 1로 바뀌고 4, 6, 10이 queue에 추가되면서
# 다음 반복때는 4, 6, 10을 기준으로 각각 -1, +1, *2를 수행
bfs()