import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
dp = arr[:]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] + arr[i], dp[i])
print(max(dp))