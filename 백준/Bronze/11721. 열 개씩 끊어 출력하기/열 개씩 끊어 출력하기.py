N = input()
word = ''
cnt = 0
for char in N:
    word += char
    cnt += 1
    if cnt == 10:
        print(word)
        cnt = 0
        word = ''
if len(word) != 0:
    print(word)