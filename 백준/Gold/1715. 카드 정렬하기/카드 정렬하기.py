import sys
input = sys.stdin.readline
from heapq import *

N = int(input())
arr = []
heapify(arr)
for i in range(N):
    heappush(arr, int(input().strip()))
# print(arr)
if N == 1:
    print(0)
elif N == 2:
    print(arr[0] + arr[1])
else:
    answer = 0
    while True:
        x1 = heappop(arr)
        x2 = heappop(arr)
        x_sum = x1 + x2
        answer += x_sum
        heappush(arr, x_sum)
        if len(arr) == 1:
            break
    print(answer)