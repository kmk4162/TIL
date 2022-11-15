import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num1 = 1
for i in range(1, n + 1):
    num1 *= i

num2 = 1
for j in range(1, m + 1):
    num2 *= j

num3 = 1
for k in range(1, n - m + 1):
    num3 *= k
# print(num1, num2, num3)
print(num1 // num2 // num3)