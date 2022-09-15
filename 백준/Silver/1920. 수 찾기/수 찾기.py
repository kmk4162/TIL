import sys
input = sys.stdin.readline

N = int(input())
Ndict = {}
temp = list(map(int, input().split()))
for i in temp:
    Ndict[i] = Ndict.get(i, 0) + 1

M = int(input())
mlist = list(map(int, input().split()))
for j in mlist:
    if j not in Ndict.keys():
        print(0)
    else:
        print(1)