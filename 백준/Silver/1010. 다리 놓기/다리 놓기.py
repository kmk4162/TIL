import sys
input = sys.stdin.readline

T = int(input())
dp = [[0] * (30) for i in range(30)]
for i in range(1, len(dp)):
    for j in range(i, len(dp)):
        if i == 1:
            dp[i][j] = j
            continue
        elif i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i][j-1] * j // (j - i)


for i in range(T):
    N, M = map(int, input().split())
    print(dp[N][M])
