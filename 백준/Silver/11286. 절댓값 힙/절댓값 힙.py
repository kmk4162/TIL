from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    num = int(input())
    if num != 0:
        heappush(heap, [abs(num), num])
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap)[1])

