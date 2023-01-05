import sys
input = sys.stdin.readline

answer = 0
card_list = []
card_dict = {}
num_list = [0] * 10
num_dict = {}
for i in range(5):
    color, num = input().split()
    num_list[int(num)] += 1
    card_dict[color] = card_dict.get(color, 0) + 1
    card_list.append((color, int(num)))
    num_dict[int(num)] = num_dict.get(int(num), 0) + 1

card_list.sort(key = lambda x : x[1])
color_count = len(card_dict) # 색깔 개수
# 연속 여부, 숫자 개수
is_continue = False
cnt = 0
number_cnt = 0
large_number = 0
for i in range(1, 10):
    if num_list[i] != 0:
        cnt += 1
        number_cnt += 1
        large_number = i
    else:
        cnt = 0
    if cnt == 5:
        is_continue = True

if color_count == 1 and is_continue:
    answer = 900 + large_number
elif max(num_list) == 4:
    for i in range(len(num_list)):
        if num_list[i] == 4:
            answer = 800 + i
            break
elif max(num_list) == 3 and 2 in num_list: 
    answer = 700 + (num_list.index(3) * 10) + num_list.index(2)
elif color_count == 1:
    answer = 600 + card_list[-1][1]
elif is_continue:
    answer = 500 + card_list[-1][1]
elif 3 in num_list:
    answer = 400 + num_list.index(3)
elif 2 in num_list and number_cnt == 3:
    low_num = 0
    high_num = 0
    flag = False
    for i in range(1, 10):
        if num_list[i] == 2:
            if flag:
                high_num = i
            else:
                low_num = i
                flag = True
    answer = 300 + (10 * high_num) + low_num
elif 2 in num_list and number_cnt == 4:
    answer = 200 + num_list.index(2)
else:
    answer = 100 + large_number
print(answer)