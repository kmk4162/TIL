import sys
input = sys.stdin.readline

xdict = {}
ydict = {}
for i in range(3):
    x, y = map(int, input().split())
    xdict[x] = xdict.get(x, 0) + 1
    ydict[y] = ydict.get(y, 0) + 1
xlocation = 0
ylocation = 0
for i in xdict.items():
    if i[1] == 1:
        xlocation = i[0]
for j in ydict.items():
    if j[1] == 1:
        ylocation = j[0]
print(xlocation, ylocation)