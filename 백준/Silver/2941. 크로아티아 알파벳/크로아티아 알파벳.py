cro_words = ['nj', 'c=', 'c-', 'dz=', 'd-', 'lj', 's=', 'z=']

word = input()
cnt = 0
for i in cro_words:
    if i in word:
        cnt += word.count(i)
print(len(word) - cnt)