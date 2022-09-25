import sys
input = sys.stdin.readline

word = input().rstrip()
word_dict = {}

for word_length in range(1, len(word) + 1):
    start_idx = 0
    while True:
        word_part = word[start_idx : start_idx + word_length]
        word_dict[word_part] = 1
        if start_idx + word_length == len(word):
            break
        start_idx += 1
# print(word_dict)
print(len(word_dict))