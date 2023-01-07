import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
arr = list(map(int, input().split()))
arr.sort()

diff_list = []
for i in range(N - 1):
    diff_list.append(arr[i + 1] - arr[i])
diff_list.sort(reverse = True)
print(sum(diff_list[K - 1:]))  