import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
answer = int(10e12)
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

for i in range(1, N + 1):
    for j in combinations(arr, i):
        S = 1
        B = 0
        for k in j:
            S *= k[0]
            B += k[1]
        if answer > abs(S - B):
            answer = abs(S - B)
print(answer)