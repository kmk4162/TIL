import sys
input = sys.stdin.readline

N = int(input())
words = list(map(int, input().split()))
answer = list(set(words))
answer.sort()
num_dict = {}
for idx in range(len(answer)):
    num_dict[answer[idx]] = idx

for num in words:
    print(num_dict[num], end = ' ')