import sys
input = sys.stdin.readline

T = int(input())
dp = [0] * 12
for case in range(T):
    N = int(input())
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    if N == 1:
        print(1)
        continue
    if N == 2:
        print(2)
        continue
    if N == 3:
        print(4)
        continue
    for i in range(4, N + 1):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    print(dp[N])