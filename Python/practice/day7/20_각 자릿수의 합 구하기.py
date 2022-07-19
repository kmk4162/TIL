# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요.

num = int(input())
result = 0
while num > 0:
    a = num // 10
    b = num % 10
    result += b
    num = a
print(result)

