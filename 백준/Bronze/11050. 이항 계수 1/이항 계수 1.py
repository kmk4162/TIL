import sys, math
input = sys.stdin.readline

a, b = map(int, input().split())
x = math.factorial(a)
y = math.factorial(a-b) * math.factorial(b)
print(int(x / y))