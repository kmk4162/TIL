import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())
answer = list(permutations(range(1, N + 1), M))

for data in answer:
    if data == tuple(sorted(data)):
        for char in data:
            print(char, end =' ')
        print()