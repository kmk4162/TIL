import sys, heapq
input = sys.stdin.readline

phone_num, concent_num = map(int, input().split())
times = list(map(int, input().split()))
times.sort(reverse = True)
# 콘센트 개수만큼의 우선순위큐 만들기
concents = [0] * concent_num
heapq.heapify(concents)

for time in times:
    concents[0] += time
    heapq.heapify(concents)
print(max(concents))