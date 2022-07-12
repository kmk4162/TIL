import sys

N, X = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))
list1 = []

for i in A:
    if i < X:
        list1.append(i)
print(*list1)
