import sys
input = sys.stdin.readline

N, K, S = map(int, input().split())
home_left = []
home_right = []
for _ in range(N):
    i, j = map(int, input().split())
    # 거리랑 위치 정보 같이 넣기
    if i > S:
        home_right.append([abs(i - S), j])
    elif i < S:
        home_left.append([abs(i - S), j])

home_left.sort()
home_right.sort()
# print(home_left)
# print(home_right)

def check(arr: list):
    cnt = 0
    while arr:
        cnt += arr[-1][0]
        bus_max = K
        while bus_max and arr:
            if arr[-1][1] > bus_max:
                arr[-1][1] -= bus_max
                bus_max = 0
            else:
                bus_max -= arr[-1][1]
                arr.pop()
    return cnt * 2

answer = check(home_left) + check(home_right)
print(answer)