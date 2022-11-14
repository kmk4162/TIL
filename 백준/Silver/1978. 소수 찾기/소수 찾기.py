import sys
input = sys.stdin.readline

# 범위가 1000 이하니까 100개 다 세주고 in으로 풀자
arr = [False for _ in range(1001)]
N = int(input())
numbers = list(map(int, input().split()))

# 소수 판별
arr[0] = True
arr[1] = True
root = int(1000 * 0.5)
for i in range(2, root + 1):
    if arr[i] == False:
        for j in range(i*2, 1001, i):
            arr[j] = True
# print(arr)
cnt = 0
for num in numbers:
    if arr[num] == False:
        cnt += 1
print(cnt)