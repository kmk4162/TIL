import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
# 같은 지점은 1
# 중앙에서 이동하면 2
# 인접한 방향으로 움직이면 3
# 반대면 4
def move(start, end):
    if start == end:
        return 1
    elif start == 0:
        return 2
    elif abs(start - end) == 1 or abs(start - end) == 3:
        return 3
    else:
        return 4

# 풀이 참고
INF = 10e6
dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(len(arr) + 1)]
dp[0][0][0] = 0

for i in range(1, len(arr)):
    target = arr[i - 1] # 움직여야할 위치
    for left in range(5):
        for right in range(5):
            # 왼발 움직이는 경우
            dp[i][target][right] = min(dp[i][target][right], dp[i - 1][left][right] + move(left, target))
            # 오른발 움직이는 경우
            dp[i][left][target] = min(dp[i][left][target], dp[i - 1][left][right] + move(right, target))

result = INF
for i in range(5):
    for j in range(5):
        result = min(result, dp[len(arr) - 1][i][j])
print(result)