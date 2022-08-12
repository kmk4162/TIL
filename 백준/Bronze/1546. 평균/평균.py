n = int(input())
word = list(map(int, input().split()))
number = max(word)
result = 0
for i in word:
    cur = i / number * 100
    result += cur
print(result / n)