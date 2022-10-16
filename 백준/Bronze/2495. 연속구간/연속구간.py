for i in range(3):
    cnt = 0
    number = input()
    cnts = []
    cur = number[0]
    for char in number:
        if char == cur:
            cnt += 1
            cur = char
        else:
            cnts.append(cnt)
            cnt = 1
            cur = char
    # 다 끝나고 남은 cnt도 추가
    cnts.append(cnt)
    print(max(cnts))