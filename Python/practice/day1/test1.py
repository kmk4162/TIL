# x = 10, y = 20일 때
# 각각 값을 바꾸어서 저장하기

x = 10
y = 20

#* 1. 임시 변수 활용
temp = y
y = x
x = temp
print(x, y)

#* 2. Pythonic하게 풀기
x,y = y, x
print(x, y) 