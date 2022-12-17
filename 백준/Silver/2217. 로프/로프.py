import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 100001

arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)
dp[1] = arr[0]
if N == 1:
    print(dp[1])
else:
    for i in range(2, N + 1):
        dp[i] = max(dp[i-1], i * arr[i - 1])
    print(max(dp))