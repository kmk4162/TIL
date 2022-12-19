import sys
input = sys.stdin.readline

N = int(input())
dp = [[0]*10 for _ in range(N + 1)]

for i in range(10):
    dp[1][i] = 1
    if N != 1:
        dp[2][i] = 10 - i
if N == 1:
    print(sum(dp[1]) % 10007)
elif N == 2:
    print(sum(dp[2]) % 10007)
else:
    for i in range(3, N + 1):
        for j in range(10):
            dp[i][j] = sum(dp[i-1][j:])
    print(sum(dp[N]) % 10007)