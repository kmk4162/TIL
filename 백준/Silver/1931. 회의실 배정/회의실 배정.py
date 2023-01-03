import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(tuple(map(int, input().split())))

dp = [0] * (N + 1)
arr.sort(reverse = True)
answer = 0
dp[0] = 1
now_start_time = arr[0][0]
for i in range(1, N):
    # i == 2
    if arr[i][1] <= now_start_time:
        dp[i] = dp[i - 1] + 1
        now_start_time = arr[i][0]
    else:
        dp[i] = dp[i - 1]
print(max(dp))