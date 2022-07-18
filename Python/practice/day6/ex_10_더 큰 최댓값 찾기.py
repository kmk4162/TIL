# 아래 코드는 리스트에서 최댓값을 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

#* Before

number_list = [1, 23, 9, 6, 91, 59, 29]
max = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")

# 무슨 에러?
#! TypeError: 'int' object is not callable

# 이유
# 예약어를 변수명으로 사용했기 때문에 발생
# max()가 존재하는데 변수를 max로 사용했기 때문에 변수 이름을 바꾸자!
#* ------------------------------------------------------------------------------

#* After

number_list = [1, 23, 9, 6, 91, 59, 29]
big1 = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
big2 = max(number_list2)

if big1 > big2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif big1 < big2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")




