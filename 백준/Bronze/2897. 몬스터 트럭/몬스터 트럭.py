from pprint import pprint
R, C = map(int, input().split())
field = []
for i in range(R):
    field.append(input())

# 맨 윗쪽 꼭짓점 기준으로 자기자신, 오른쪽, 밑, 우하향 델타
delta = [(0, 0), (0, 1), (1, 0), (1, 1)]

# 한대도 안 부수고 주차 가능 개수 부터 네대를 부수고 주차할 수 있는 개수 
# 카운트는 총 5개; 4칸 안에 X가 0개있냐, 1개있냐 ... 4개있냐로 체크
count_break = [0, 0, 0, 0, 0]

for x in range(0, R - 1):
    for y in range(0, C - 1):
        count_X = 0
        count_sharp = 0
        for d in range(4):
            row = x + delta[d][0]
            col = y + delta[d][1]
            # 각 칸에 뭐가 있는지 체크
            if field[row][col] == 'X':
                count_X += 1
            elif field[row][col] == '#':
                count_sharp += 1
        # 몇 대를 부숴야 가능한지 경우의 수 세기
        # #이 2개 있다면 2개를 부숴야 주차 가능하므로 count_break의 인덱스 2에 +1를 하는 방식
        #! #이 한개라도 있으면 불가능하므로 #이 0개 일때만 추가
        if count_sharp == 0:
            count_break[count_X] += 1
for cnt in count_break:
    print(cnt)


