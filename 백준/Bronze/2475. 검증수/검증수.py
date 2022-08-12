numbers = list(map(int, input().split()))
result = 0
for i in numbers:
    result += i ** 2
print(result % 10)
