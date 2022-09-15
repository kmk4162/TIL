T = int(input())

for i in range(T):
    word = input()
    new_word = []
    for j in word:
        if j == 'b':
            new_word.append('d')
        elif j == 'd':
            new_word.append('b')
        elif j == 'p':
            new_word.append('q')
        else:
            new_word.append('p')
    # b랑 d, p랑 q끼리 서로 바꿔서 새 문자열 리스트에 넣고
    new_word = ''.join(new_word)
    # join으로 문자열로 합쳐서 만듦
    print(f'#{i + 1} {new_word[::-1]}')
    # 거울은 반대로 보이면서 순서도 바뀌니까 거꾸로 슬라이싱