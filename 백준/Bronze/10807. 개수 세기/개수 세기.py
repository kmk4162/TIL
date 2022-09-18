import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
print(nums.count(int(input())))