import sys
input = sys.stdin.readline
from heapq import *

N = int(input())
arr = []
for i in range(N):
    cmd = int(input())
    if cmd == 0:
        if not arr:
            print(0)
        else:
            print(heappop(arr) * (-1))
    else:
        heappush(arr, cmd * (-1))