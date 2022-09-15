cnt = 0
while True:
    cnt += 1
    T = int(input())
    text = list(map(str, input().split()))
    # text = ['449047', '855428', '425117', '532416', '358612', 
    # '929816', '313459', '311433', '472478', '589139', '568205']
    command_number = int(input())
    # command_number만큼 삽입을 반복
    commands = input().split('I')
    
    for i in range(1, len(commands)):
        x = commands[i].split()
        # x = ['1', '5', '400905', '139831', '966064', '336948', '119288']
        # 를 공백 기준으로 나눔
        index = int(x[0])
        # text에 삽입할 위치
        lefttext = text[:index]
        # index 기준으로 왼쪽 리스트에 요소를 순서대로 추가하기
        insert_nums = x[2:]
        # insert_nums = ['400905', '139831', '966064', '336948', '119288']
        for j in insert_nums:
            lefttext.append(j)
        # insert_nums 요소를 차례대로 추가
        newtext = lefttext + text[index:]
        text = newtext
        # 수정된 lefttext와 text 오른쪽을 합쳐서 newtext로 바꾸기
    result = ' '.join(text[:10])
    print(f'#{cnt} {result}')

    if cnt == 10:
        break