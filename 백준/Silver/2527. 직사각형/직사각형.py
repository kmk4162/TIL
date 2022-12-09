import sys
input = sys.stdin.readline

for i in range(4):
    squares = list(map(int, input().split()))
    square1 = squares[:4]
    square2 = squares[4:]
    # 왼쪽 밑 x값 기준으로 정렬; 어느것이 왼쪽에 있는지
    square1_x = square1[0]
    square2_x = square2[0]
    if square1_x < square2_x:
        new_squares = square1 + square2
    else:
        new_squares = square2 + square1
    # 두번째 사각형 왼쪽밑 꼭짓점의 x, y 좌표따라 조건 분기
    # 1. 아예 안 겹치는 경우
    if new_squares[2] < new_squares[4] or new_squares[3] < new_squares[5] or new_squares[1] > new_squares[7]: 
        response = 'd'
    # 2. 점으로 겹치는 경우
    elif (new_squares[2] == new_squares[4] and new_squares[3] == new_squares[5]) or (new_squares[2] == new_squares[4] and new_squares[1] == new_squares[7]):
        response = 'c'
    # 3. 선으로 겹치는 경우
    elif new_squares[2] == new_squares[4] or new_squares[1] == new_squares[7] or new_squares[3] == new_squares[5]:
        response = 'b'
    # 4. 나머지는 면적이 겹침
    else:
        response = 'a'
    print(response)