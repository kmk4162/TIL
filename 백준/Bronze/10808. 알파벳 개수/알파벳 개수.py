word = input()
wordlist = [0] * 26
for char in word:
    x = ord(char)
    wordlist[x - 97] += 1
for num in wordlist:
    print(num, end = ' ')