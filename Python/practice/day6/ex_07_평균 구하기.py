# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

#* Before

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
count += 1

print(total // count)

# 무슨 에러?
#! 에러 코드는 안 뜨지만 논리적 오류!

# 이유
# number를 받을 때마다 total에 합치면서 count도 올라가야 하는데
# 들여쓰기 때문에 for문이 다 돌고나서 count += 1가 한 번만 실행됨
# 그리고 // 는 나눗셈이 아니라 몫. 따라서 5.5가 안 나오기 때문에 /로 고쳐야함
#* ------------------------------------------------------------------------------

#* After

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    count += 1
    total += number

print(total / count)
