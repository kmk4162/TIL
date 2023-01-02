import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = N - 1
answer = abs(arr[left] + arr[right])
final = [arr[left], arr[right]]

while left < right:
    left_value = arr[left]
    right_value = arr[right]

    sum_value = left_value + right_value

    # 더한 값이 이전보다 작다면 업데이트
    if abs(sum_value) < answer: 
        answer = abs(sum_value)
        final = [left_value, right_value]
        if answer == 0:
            break
    if sum_value < 0:
        left += 1
    else:
        right -= 1
print(*final)