import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp_up = [1] * N
dp_down = [1] * N
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_up[i] = max(dp_up[j] + 1, dp_up[i])

# arr 거꾸로 해서 뒷쪽부터 감소 수열 찾기
arr_down = arr[::-1]
for i in range(N):
    for j in range(i):
        if arr_down[i] > arr_down[j]:
            dp_down[i] = max(dp_down[j] + 1, dp_down[i])
dp_down = dp_down[::-1]

answer = 0
for i in range(N):
    answer = max(answer, dp_up[i] + dp_down[i] - 1)
print(answer)