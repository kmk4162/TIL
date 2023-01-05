word = input()
word_dict = {}
for char in word:
    word_dict[char] = word_dict.get(char, 0) + 1
odd_cnt = 0
odd_alpha = ''
for key in word_dict:
    if word_dict[key] % 2 == 1:
        odd_cnt += 1
        odd_alpha += key
if odd_cnt >= 2:
    print("I'm Sorry Hansoo")
else:
    answer = ''
    for key in word_dict:
        for i in range(word_dict[key] // 2):
            answer += key
    answer = sorted(answer)
    answer = ''.join(answer)
    result = answer + odd_alpha + answer[::-1]
    print(result)