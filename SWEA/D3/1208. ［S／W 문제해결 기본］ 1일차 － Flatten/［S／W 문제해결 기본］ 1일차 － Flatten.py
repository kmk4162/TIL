for test_case in range(1, 11):
    dump = int(input())
    # 100개의 입력 받기
    field = list(map(int, input().split()))

    # 높낮이 차를 넣을 변수
    result = 0

    # 가장 큰 값과 작은 값 찾음 -> 몇번째인지 알아내기
    for i in range(dump):

        # 최대값과 그 위치 찾기
        max_value = max(field)
        max_location = field.index(max_value)

        # 최소값과 그 위치 찾기
        min_value = min(field)
        min_location = field.index(min_value)

        if max_value - min_value > 0:
            field[max_location] -= 1
            field[min_location] += 1
            result = max(field) - min(field)
        else:
            break
    print(f'#{test_case} {result}')    