# 월이 입력될 때 계절 이름이 출력되도록 해보자.

# 월 : 계절 이름
# 12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
#   9, 10, 11 : fall

month = int(input())

if month >= 3 and month <=5:
    print('spring')
elif month >= 6 and month <=8:
    print('summer')
elif month >= 9 and month <=11:
    print('fall')
elif month <= 2 or month == 12:
    print('winter')





