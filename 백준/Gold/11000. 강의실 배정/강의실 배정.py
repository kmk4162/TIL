import sys, heapq
input = sys.stdin.readline

N = int(input())
list = []
for i in range(N):
    start, end = map(int, input().split())
    list.append((start, end))
list.sort(key = lambda x : (x[0], x[1]))

# 교실 개수 우선순위 큐
class_list = []
heapq.heapify(class_list)

for time in list:
    # 시작 시간이 어느 교실의 끝나는 시간이랑 같거나 더 크다면 
    # 그 교실에서 이어서 강의가 가능
    if class_list and time[0] >= class_list[0]:
        heapq.heapreplace(class_list, time[1])
    else:
        heapq.heappush(class_list, time[1])
print(len(class_list))