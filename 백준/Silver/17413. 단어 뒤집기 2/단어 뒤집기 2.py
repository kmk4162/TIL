import sys
input = sys.stdin.readline

line = input()
tag_word = ''
in_tag = False
answer = ''
word = ''

for char in line:
    if char == '<':
        tag_word += char
        answer += word[::-1]
        word = ''
        in_tag = True
    elif char == '>':
        tag_word += char
        answer += tag_word
        tag_word = ''
        in_tag = False
    else:
        if in_tag:
            tag_word += char
        else:
            if char == ' ':
                word = word[::-1]
                answer += word
                answer += char
                word = ''
            else:
                word += char

answer += word[::-1]
print(answer.replace("\n", ""));