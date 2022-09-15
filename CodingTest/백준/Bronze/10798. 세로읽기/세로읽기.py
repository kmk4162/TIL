lines = []
for i in range(5):
    lines.append(list(map(str, input())))

# 각 줄마다 길이를 체크, 가장 큰 값을 기준으로 문자 채우기
maxlength = max(map(len, lines))

for line in lines:
    if len(line) != maxlength:
        line += '@' * (maxlength - len(line))

for i in range(maxlength):
    for j in range(5):
        if lines[j][i] != '@':
            print(lines[j][i], end = '')
        else:
            continue