T = int(input())
for i in range(1, T + 1):
    num, word = input().split()
    result = ''
    for char in word:
        result += char * int(num)
    print(result)