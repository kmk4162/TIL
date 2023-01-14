import sys
input = sys.stdin.readline

N = int(input())
line = []
for i in range(N):
    start, end = map(int, input().split())
    line.append((start, end))
line.sort(key = lambda x: x[0])
dp = [1] * (N)

def check(arr):
    for i in range(1, N):
        for j in range(i):
            if arr[i][1] > arr[j][1]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)
print(N - check(line))