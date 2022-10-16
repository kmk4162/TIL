problem = 0
duck = 0

while True:
    word = input()
    if word == '고무오리 디버깅 시작':
        continue
    elif word == '문제':
        problem += 1
    elif word == '고무오리':
        if problem == 0:
            problem = 2
        else:
            problem -= 1
    elif word == '고무오리 디버깅 끝':
        break

if problem == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')