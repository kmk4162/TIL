# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요.

num = int(input())
result = 0
while num > 0:
    #* 1. 내 풀이
    # a = num // 10
    # b = num % 10
    # result += b
    # num = a

    #* 2. divmod 사용
    #* divmod(x,y)는 x를 y로 나누고, 결과를 tuple로 반환
    numb, remainder = divmod(num, 10)
    result += remainder
print(result)



