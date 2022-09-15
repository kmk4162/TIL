import sys
input = sys.stdin.readline

result = []
for i in range(int(input())):
    result.append(int(input()))
result.sort()
for num in result:
    print(num)