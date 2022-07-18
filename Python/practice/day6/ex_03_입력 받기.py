# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

#* Before

# numbers = input().split()
# print(sum(numbers))

# 무슨 에러?
#! TypeError: unsupported operand type(s) for +: 'int' and 'str'
#@ operand : 피연산자

# 이유
# sum은 숫자끼리 더하는 함수인데 그냥 input으로 받으면 numbers는 str타입임
# 따라서 int로 자료형을 바꿔줘야함!
#* ------------------------------------------------------------------------------

#* After

numbers = map(int, input().split())
print(sum(numbers))
