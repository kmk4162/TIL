import sys
input = sys.stdin.readline

line = input().strip()
num_list = []
sign_list = []
number = ''
isNumber = False
if line[0] == '-':
    isFirstMinus = True
else:
    isFirstMinus = False
for idx in range(len(line)):
    if idx == 0 and isFirstMinus:
        continue
    if line[idx].isdigit():
        if isNumber:
            number += line[idx]
        if not isNumber:
            number = ''
            number += line[idx]
            isNumber = True
    else:
        if isFirstMinus:
            num_list.append(int(number)*(-1))
            isFirstMinus = False
        else:
            num_list.append(int(number))
        isNumber = False
        sign_list.append(line[idx])
if isFirstMinus:
    num_list.append(int(number)*(-1))
else:
    num_list.append(int(number))
# print(num_list)
# print(sign_list)
# 기호가 전부 +면 그냥 더해주고 끝내기
isAllPlus = True
for i in sign_list:
    if i == '-':
        isAllPlus = False
        break

if isAllPlus:
    print(sum(num_list))
else:
    new_num_list = []
    add_number = 0
    for i in range(len(sign_list)):
        # +끼리 더하고 -만 남을때 다 빼면 가장 작은 수
        if sign_list[i] == '+':
            add_number = num_list[i] + num_list[i+1]
            num_list[i] = 0
            num_list[i+1] = add_number
        else:
            if add_number == 0:
                new_num_list.append(num_list[i])
            else:
                new_num_list.append(add_number)
                add_number = 0
    new_num_list.append(num_list[-1])
    answer = new_num_list[0] # 초기값
    for i in range(1, len(new_num_list)):
        answer -= new_num_list[i]
    print(answer)