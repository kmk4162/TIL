import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))
coins.sort()

dp = [0] * (K + 1)
dp[0] = 1
for coin in coins:
    for i in range(coin, K + 1):
        dp[i] += dp[i - coin]
print(dp[-1])