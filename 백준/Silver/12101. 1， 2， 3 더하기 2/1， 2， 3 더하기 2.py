import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[] for _ in range(30)]

dp[1].append([1])
dp[2].append([1, 1])
dp[2].append([2])
dp[3].append([1, 1, 1])
dp[3].append([1, 2])
dp[3].append([2, 1])
dp[3].append([3])

if n >= 4:
    for i in range(4, n + 1):
        # 3번 더해주기 (점화식)
        for j in range(i - 1, i - 4, -1):
            for d in dp[j]:
                new_arr = [i - j] + d
                dp[i].append(new_arr)

if len(dp[n]) < k:
    print(-1)
else:
    target = dp[n][k - 1]
    answer = ''
    for c in target:
        answer += str(c)
        answer += '+'
    print(answer[:-1])