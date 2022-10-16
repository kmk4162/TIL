import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)
for num in range(10):
    print(result.count(str(num)))