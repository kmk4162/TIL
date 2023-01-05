import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
if K == 1:
    answer = arr[-1] - arr[0]
else:
    diff_list = []
    for i in range(len(arr) - 1):
        diff_list.append(arr[i + 1] - arr[i])
    diff_list.sort(reverse = True)
    answer = sum(diff_list[K - 1:])
print(answer)  