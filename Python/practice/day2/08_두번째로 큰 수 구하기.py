# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
#! max() 함수 사용 금지

#* cases
numbers = [0, 1, 0] 
# numbers = [0, 20, 100, 50, -60, 50, 100] 
# numbers = [0, 20, 100]
# numbers = [-10, -100, -30] 

first_big = numbers[0]
second_big = numbers[0]
#? first_big = float("-inf")
#? second_big = float("-inf") 이렇게도 가능!!
cnt = 0

for i in numbers:
    cnt += 1
    if i > first_big:
        second_big = first_big
        first_big = i
    elif i == first_big:
        continue
    elif i > second_big:
        second_big = i
    elif i < second_big:
        if first_big == second_big:
            first_big = second_big
            second_big = i
    print(first_big, second_big, cnt)
print(second_big)