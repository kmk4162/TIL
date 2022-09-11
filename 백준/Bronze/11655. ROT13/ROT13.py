line = input()
answer = ''
for char in line:
    if char == ' ':
        answer += char
    elif 48 <= ord(char) <= 57:
        answer += char
    elif 65 <= ord(char) <= 77:
        answer += chr(ord(char) + 13)
    elif 78 <= ord(char) <= 90:
        answer += chr(ord(char) - 13)
    elif 97 <= ord(char) <= 109:
        answer += chr(ord(char) + 13)
    elif 110 <= ord(char) <= 122:
        answer += chr(ord(char) - 13)
print(answer)