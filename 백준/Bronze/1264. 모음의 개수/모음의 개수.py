moeum = ['a', 'e', 'i', 'o', 'u']
while True:
    count = 0
    word = input().lower()
    if word == '#':
        break
    else:
        for char in word:
            if char in moeum:
                count += 1
    print(count)