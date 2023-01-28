import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

# 4 3 3 2
for i in range(1, N + 1):
    arr[i - 1] = arr[i - 1] - i
# print(arr)
print(2 + len(arr) + max(arr))