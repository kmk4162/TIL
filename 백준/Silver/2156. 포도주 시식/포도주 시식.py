N = int(input())
wine = []
for i in range(N):
    wine.append(int(input()))
dp = [0] * N
dp[0] = wine[0]
if N > 1:
    dp[1] = wine[0] + wine[1]
if N > 2:
    dp[2] = max(dp[1], wine[0] + wine[2], wine[1] + wine[2])
for i in range(3, N):
    dp[i] = max(dp[i - 2] + wine[i], wine[i -1] + wine[i] + dp[i - 3], dp[i - 1])
print(max(dp))