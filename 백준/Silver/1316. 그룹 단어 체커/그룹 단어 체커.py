N = int(input())
count = 0
for _ in range(N):
    word = input()
    worddict = {word[0] : 0}
    before = word[0]
    for char in word:
        # 이전과 같은지 아닌지 비교
        if char == before:
            worddict[char] += 1
            before = char
        else:
            if char in worddict:
                break
            else:
                worddict[char] = 1
                before = char
    else:
        count += 1
print(count)