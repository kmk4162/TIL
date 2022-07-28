# C A M B R I D G E 삭제

ban_list =['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
word = input()
new_word = []
for i in word:
    if i in ban_list:
        continue
    else:
        new_word.append(i)
print(''.join(new_word))