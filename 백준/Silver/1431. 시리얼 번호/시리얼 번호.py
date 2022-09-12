import sys
input = sys.stdin.readline

# 길이가 짧을수록, 자릿수 합이 적을수록, 사전순(숫자가 알파벳보다 앞)
N = int(input())
words = {}
for i in range(N):
    word = input().rstrip()
    cnt = 0
    for char in word:
        if '0' <= char <= '9':
            cnt += int(char)
    words[word] = (len(word), cnt)
    
result = sorted(words.items(), key = lambda x : (x[1][0], x[1][1], x[0]))
for i in result:
    print(i[0])