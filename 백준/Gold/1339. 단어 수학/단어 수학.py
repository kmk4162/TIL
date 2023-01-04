import sys
input = sys.stdin.readline

N = int(input())
arr = []
numbers = list(range(9, -1, -1))
for i in range(N):
    arr.append(input().strip())

new_arr = {}
for word in arr:
    for i in range(len(word)):
        if word[i] not in new_arr:
            new_arr[word[i]] = 10 ** (len(word) - i - 1)
        else:
            new_arr[word[i]] += 10 ** (len(word) - i - 1)
alpha = []
for i in new_arr:
    alpha.append((i, new_arr[i]))
alpha.sort(reverse = True, key = lambda x: x[1])
answer = 0
cnt = 9
for j in alpha:
    answer += cnt * j[1]
    cnt -= 1
print(answer)