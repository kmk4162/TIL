T = int(input())

for test_case in range(1, T + 1):
    cards_num = int(input())
    cardlist = list(input().split())

    # input이 짝수면 그대로, 홀수면 한장 많은쪽이 맨 위에 덱에 오게
    # left와 right로 카드를 나눔
    center = cards_num // 2
    # 짝수일 때
    if cards_num % 2 == 0:
        left = cardlist[0:center]
        right = cardlist[center:]
        print(f'#{test_case}', end = ' ')
        for i in range(center):
            print(left[i], end = ' ')
            print(right[i], end = ' ')
        print()

    # 홀수일 때
    else:
        left = cardlist[0:center + 1]
        right = cardlist[center + 1:]
        print(f'#{test_case}', end = ' ')
        for i in range(center + 1):
            print(left[i], end = ' ')
            if i == center:
                break
            else:
                print(right[i], end = ' ')
        print()
