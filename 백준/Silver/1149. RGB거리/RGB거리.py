import sys
input = sys.stdin.readline

N = int(input())
rgb = []
for i in range(N):
    r, g, b = map(int, input().split())
    rgb.append((r, g, b))
# 1번 접근법
# dp1 = [], dp2 = [], dp3 = [] 이렇게 있을때
# dp1이 R, dp2가 G, dp3가 B로 시작하는 경우
# N = 3일경우, 121, 123, 131, 132를 해서 가장 낮은 값 갱신 -> dp1의 최솟값
# 마찬가지로 dp2, dp3의 최솟값을 구한다음, 셋 중 가장 낮은 값 구하기?

# 2번 접근법
dp = [[0] * 3 for i in range(N)]
# 첫째줄 초기값
dp[0][0] = rgb[0][0]
dp[0][1] = rgb[0][1]
dp[0][2] = rgb[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]
# print(dp)
print(min(dp[-1]))