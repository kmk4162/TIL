import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
cnt = 0
for i in range(N):
    cnt += A[i] * B[i]
print(cnt)