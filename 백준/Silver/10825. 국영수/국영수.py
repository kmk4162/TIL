import sys, math
input = sys.stdin.readline

N = int(input())
scores = []
for i in range(N):
    data = input().split()
    scores.append((data))
x = sorted(scores, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for j in x:
    print(j[0])