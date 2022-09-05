import sys
input = sys.stdin.readline

N = int(input())
nums = [0] * 10001
for i in range(N):
    nums[int(input())] += 1
for j in range(10001):
    if nums[j] != 0:
        for k in range(nums[j]):
            print(j)