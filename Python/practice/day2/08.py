# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

# 이 문제는 다시 한 번 보자!

numbers = [-10, -100, -30]
first_big = numbers[0]
second_big = numbers[0]
cnt = 0

for i in numbers:
    cnt += 1
    if i > first_big:
        second_big = first_big
        first_big = i
    elif i >= second_big:
        if i == first_big:
            first_big == i
        else:
            second_big = i
    elif i < second_big:
        if first_big == second_big:
            second_big = i
    print(f'{cnt}번째')
    print(f'현재까지 가장 큰 수는 {first_big}이고')
    print(f'현재까지 두번째로 큰 수는 {second_big}입니다')
    print('--------------------------------------------------------')
print(f'따라서 두번째로 큰 수는 {second_big} 입니다!')