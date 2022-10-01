import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    N = int(input())
    numdict = {}
    for n in list(map(int, input().split())):
        numdict[n] = numdict.get(n, 0) + 1
    M = int(input())
    for m in list(map(int, input().split())):
        if m in numdict:
            print(1)
        else:
            print(0)