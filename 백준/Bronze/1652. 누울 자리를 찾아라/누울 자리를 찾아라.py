n = int(input())
room = []
for _ in range(n):
    x = list(input())
    room.append(x)

# 행 기준 체크
result_row = 0
for row in room:
    cnt_row = 0
    cnt_empty = 0
    string_row = ''.join(row) # 한줄씩 문자열로 인식시키기 위해
    # . . . X . . 이렇게 들어온다고 가정
    for char in string_row: # 문자열의 글자 하나하나씩 순회
        if char == '.':
            cnt_empty += 1
        else:
            cnt_empty = 0 # X가 들어오면 초기화 시켜야함 (더 이상 못 뻗음)
        if cnt_empty == 2:
            cnt_row += 1
    result_row += cnt_row
print(result_row, end = ' ')

# 열 기준으로 순회하기 위해
# room을 세로 기준으로 정렬한 new_room으로 바꾸기
new_room = []
for y in range(n):
    col = []
    for x in range(n):
        col.append(room[x][y])
    new_room.append(col)

# 이제 열 기준 순회    
result_col = 0
for col in new_room:
    cnt_col = 0
    cnt_empty = 0
    string_col = ''.join(col) # 한줄씩 문자열로 인식시키기 위해
    for char in string_col: # 문자열의 글자 하나하나씩 순회
        if char == '.':
            cnt_empty += 1
        else:
            cnt_empty = 0 # X가 들어오면 초기화 시켜야함 (더 이상 못 뻗음)
        if cnt_empty == 2:
            cnt_col += 1
    result_col += cnt_col
print(result_col, end = ' ')