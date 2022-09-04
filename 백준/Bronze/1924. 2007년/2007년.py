days =['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

month, day = map(int, input().split())
day31 = [1, 3, 5, 7, 8, 10, 12]
day30 = [4, 6, 9, 11]
day28 = [2]

cnt_month = 1
cnt_day = 0

while True:
    if cnt_month == month:
        break
    if cnt_month in day31:
        cnt_day += 31
    elif cnt_month in day30:
        cnt_day += 30
    elif cnt_month in day28:
        cnt_day += 28
    cnt_month += 1    
# 총 일수 구하기
cnt_day += day

result = (cnt_day % 7)
print(days[result])