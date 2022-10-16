import sys, heapq
input = sys.stdin.readline

array = []
# N은 기간, M은 선호도의 합, K는 종류
N, M, K = map(int, input().split())
for i in range(K):
    # 선호도, 도수 순서대로 저장
    priority, alcohol = map(int, input().split())
    array.append((priority, alcohol))
array.sort(key = lambda x : (x[1], x[0]))

heap = []
priority_sum = 0
alcohol_sum = 0
for i in range(K):
    priority_sum += array[i][0]
    heapq.heappush(heap, array[i][0])
    if len(heap) == N:
        if priority_sum >= M:
            print(array[i][1])
            break
        else:
            priority_sum -= heapq.heappop(heap)
else:
    print(-1)