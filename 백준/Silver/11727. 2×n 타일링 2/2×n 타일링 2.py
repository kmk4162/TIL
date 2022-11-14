import sys
input = sys.stdin.readline

dp = [0 for _ in range(1001)]
N = int(input())
dp[1] = 1
dp[2] = 3
dp[3] = 5
dp[4] = 11
# 1 + (4 * 2) + (1 + 2 + 1) * 3
# 1 + (5 * 2) + (1 + 2 + 1) * 6 + (1 + 6 + 1)

def tile(x):
    if 1 <= x <= 4:
        return dp[x]
    if dp[x] != 0:
        return dp[x]
    dp[x] = tile(x - 2) * 2 + tile(x - 1)
    return dp[x]
print(tile(N) % 10007)