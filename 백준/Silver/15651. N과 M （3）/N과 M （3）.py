import sys
input = sys.stdin.readline
from itertools import product

N, M = map(int, input().split())
answer = list(product(range(1, N + 1), repeat = M))
for data in answer:
    print(*data)