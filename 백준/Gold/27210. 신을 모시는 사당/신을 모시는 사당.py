import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp_1 = [0] * N
dp_2 = [0] * N

for i in range(N):
    if arr[i] == 1:
        dp_1[i] = dp_1[i - 1] + 1
        dp_2[i] = max(0, dp_2[i - 1] - 1)
    else:
        dp_1[i] = max(0, dp_1[i - 1] - 1)
        dp_2[i] = dp_2[i - 1] + 1

print(max(max(dp_1), max(dp_2)))