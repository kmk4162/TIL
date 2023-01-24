import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [(0, 0)] # 초기값
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort()

dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = arr[i][0]
        v = arr[i][1]

        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[N][K])