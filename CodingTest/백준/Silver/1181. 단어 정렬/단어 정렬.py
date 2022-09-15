import sys
input = sys.stdin.readline

N = int(input())
words = {}
for i in range(N):
    word = input().rstrip()
    if not word in words:
        words[word] = len(word)
result = sorted(words.items(), key = lambda x : (x[1], x[0]))
for j in result:
    print(j[0])