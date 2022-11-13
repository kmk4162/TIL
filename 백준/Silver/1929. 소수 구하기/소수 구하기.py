import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [True] * (m + 1)
root = int(m ** 0.5)

for i in range(2, root + 1):
    if arr[i] == True:
        # 배수 만큼
        for j in range(i + i, m + 1, i):
            arr[j] = False
# print(arr)
# 얘는 없는 0을 False 처리
arr[0] = False
# 1은 소수가 애초에 아니니까 False 처리
arr[1] = False

for i in range(n, m + 1):
    if arr[i] == True and i >= n and i <= m:
        print(i)