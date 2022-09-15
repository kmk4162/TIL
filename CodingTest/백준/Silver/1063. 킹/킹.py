# 기본 체스판
chess = [['0'] * 8 for i in range(8)]

# 가로 세로 좌표 위한 리스트
columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
rows = ['8', '7', '6', '5', '4', '3', '2', '1']

# 상 부터 시계방향으로 8방향
# 만약 입력이 RB로 들어온다면 딕셔너리를 통해 (1,1)의 델타에 접근가능
directions = {'T' : (-1, 0), 
              'RT' : (-1, 1), 
              'R' : (0, 1), 
              'RB' : (1, 1), 
              'B' : (1, 0), 
              'LB' : (1, -1), 
              'L' : (0, -1), 
              'LT' : (-1, -1)
}
# x = 'A2'
# print(list(''.join(x))) # ['A', '2'] 로 나눌 수 있음

# 입력 받기
king, stone, N = input().split()

# 일단 위치 먼저 (그 후 반복에서도 항상 위치 업데이트)
#* 킹
king_now = list(''.join(king))
ky = columns.index(king_now[0]) # A2가 현재위치일때 king_now[0]이 'A', A의 인덱스를 변수에 저장
kx = rows.index(king_now[1])
chess[kx][ky] = '#'
#* 돌
stone_now = list(''.join(stone))
sy = columns.index(stone_now[0]) 
sx = rows.index(stone_now[1])
chess[sx][sy] = '@'

# 킹은 '#', 돌은 '@'로 두고 이동시키기
for i in range(int(N)):
    # 킹 명령 받기
    cmd = directions[input()]

    # 킹이 이동하고 범위가 안맞으면 continue
    new_ky = ky + cmd[1]
    new_kx = kx + cmd[0]
    if not (-1 < new_ky < 8 and -1 < new_kx < 8):
        continue
    # 이동 후 돌이랑 위치가 다르면 그대로, 같으면 돌도 똑같이 이동
    if new_kx == sx and new_ky == sy:
        new_sx = sx + cmd[0]
        new_sy = sy + cmd[1]
        # 이동 후 범위를 넘어서면 무효
        if not (-1 < new_sy < 8 and -1 < new_sx < 8):
            continue
        # 이 경우는 킹이 이동했는데 범위안에 있고, 돌의 위치랑 같아져서 똑같이 돌도 이동시켰는데
        # 돌도 범위 안에 잘 있는 경우 -> 제대로 업데이트
        else:
            chess[kx][ky] = '0'
            chess[sx][sy] = '0'
            chess[new_kx][new_ky] = '#'
            chess[new_sx][new_sy] = '@'
            kx, ky = new_kx, new_ky
            sx, sy = new_sx, new_sy
    # 이동했는데 돌과 위치가 안 겹쳐서 그냥 킹만 업데이트
    else:
        chess[kx][ky] = '0'
        chess[new_kx][new_ky] = '#'
        kx, ky = new_kx, new_ky
# 최종적으로 ky, kx, sy, sx 숫자를 chess에 접근해서 좌표를 얻어내기
# pprint(chess)
print(columns[ky], rows[kx], sep = '')
print(columns[sy], rows[sx], sep = '')