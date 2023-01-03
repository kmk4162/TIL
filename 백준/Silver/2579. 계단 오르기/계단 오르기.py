N = int(input())
arr = []
arr.append(0)
for i in range(N):
    arr.append(int(input()))
dp = [0] * (N + 1)

dp[1] = arr[1]
if N >= 2:
    dp[2] = arr[1] + arr[2]
if N >= 3:
    dp[3] = max(arr[1] + arr[3], arr[2] + arr[3])
for i in range(4, N + 1):
    dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i])
if N == 3:
    print(dp[3])
else:
    print(dp[-1])