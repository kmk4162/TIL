import sys
input = sys.stdin.readline

result = []
for i in range(int(input())):
    result.append(tuple(map(int, input().split())))
result.sort(key = lambda x : (x[1], x[0]))
for elem in result:
    print(elem[0], elem[1])