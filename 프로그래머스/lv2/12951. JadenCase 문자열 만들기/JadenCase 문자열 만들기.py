def solution(s):
    isword = False
    word = ''
    answer = ''
    for char in s:
        if char == ' ':
            if isword:
                if 48 <= ord(word[0]) <= 57:
                    newword = word[0] + word[1:].lower()
                else:
                    newword = word[0].upper() + word[1:].lower()
                answer += newword
                answer += ' '
                word = ''
                isword = False
            else:
                answer += ' '
        else:
            isword = True
            word += char
    if s[-1] != ' ':
        if 48 <= ord(word[0]) <= 57:
            newword = word[0] + word[1:].lower()
        else:
            newword = word[0].upper() + word[1:].lower()
        answer += newword
    return answer