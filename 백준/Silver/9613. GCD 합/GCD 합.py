import sys
input = sys.stdin.readline
from itertools import combinations

def gcd(x, y):
    if y == 0:
        return x
    if x == y:
        return y
    else:
        return gcd(y, x % y)

T = int(input())
for _ in range(T):
    line = list(map(int, input().split()))
    N = line[0]
    arr = line[1:]
    cnt = 0
    for i in combinations(arr, 2):
        cnt += gcd(i[0], i[1])
    print(cnt)