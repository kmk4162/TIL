from itertools import *

N, M = map(int, input().split())
numlist = [i for i in range(1, N + 1)]
result = list(permutations(numlist, M))
for data in result:
    print(*data)