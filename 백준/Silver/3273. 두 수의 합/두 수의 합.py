import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
X = int(input())

start = 0
end = N - 1
cnt = 0

while start < end:
    sum_val = arr[start] + arr[end]
    if sum_val == X:
        cnt += 1

    if sum_val <= X:
        start += 1
    else:
        end -= 1

print(cnt)