import sys, heapq
input = sys.stdin.readline

# N은 자리수
N = int(input())
# N이 3이면 000, 001, ..., 111 까지
dp = [0] * 91
dp[0] = 0
dp[1] = 1
dp[2] = 1
for i in range(3, 91):
    dp[i] = dp[i-1] + dp[i-2]
    if N == i:
        break
print(dp[N])