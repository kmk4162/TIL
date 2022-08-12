word = input()
count_list = [-1] * 26
cnt = 0
for i in word:
    num = ord(i) - 97
    if count_list[num] == -1:
        count_list[num] = cnt
    cnt += 1
print(*count_list)