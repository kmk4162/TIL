T = int(input())

for test_case in range(T):
    words = {}
    cnt = 0
    result = 0
    word = input()
    for char in word:
        words[char] = words.get(char, 0) + 1
    for i in words:
        if words[i] == 2:
            cnt += 1
    if len(words) == 2 and cnt == 2:
        result = 'Yes'
    else:
        result = 'No'
    print(f'#{test_case + 1} {result}')