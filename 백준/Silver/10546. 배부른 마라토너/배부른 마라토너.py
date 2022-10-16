from collections import deque
import sys
input = sys.stdin.readline

n_dict = {}
n = int(input())

for _ in range(n):
    runner = input()
    n_dict[runner] = n_dict.get(runner, 0) + 1
# 딕셔너리 만들기(동명이인 고려)

for _ in range(n-1):
    n_dict[input()] -= 1

for k, v in n_dict.items():
    if v == 1:
        print(k)

