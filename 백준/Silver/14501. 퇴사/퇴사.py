import sys
input = sys.stdin.readline

N = int(input())
time = [0] * (N + 1)
pay = [0] * (N + 1)
for i in range(N):
    t, p = map(int, input().split())
    time[i] = t
    pay[i] = p
    
dp = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    # 새작업을 추가할수 있나 없나
    if time[i] + i  <= N:
        dp[i] = max(dp[i + 1], pay[i] + dp[time[i] + i])
    else:
        dp[i] = dp[i + 1]
print(dp[0])