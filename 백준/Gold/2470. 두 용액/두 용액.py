import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = N - 1
answer = 1e12
answer_list = [0, 0]

while left < right:
    now_val = arr[left] + arr[right]
    if abs(now_val) < answer:
        answer = abs(now_val)
        answer_list = [arr[left], arr[right]]

    if now_val < 0:
        left += 1
    else:
        right -= 1

print(*answer_list)