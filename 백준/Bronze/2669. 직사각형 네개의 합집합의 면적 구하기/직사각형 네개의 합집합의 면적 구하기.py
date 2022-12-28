import sys
input = sys.stdin.readline

white_board = [[0] * 101 for _ in range(101)]
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for row in range(x1, x2):
        for col in range(y1, y2):
            white_board[row][col] = 1
cnt = 0
for i in range(101):
    for j in range(101):
        if white_board[i][j] == 1:
            cnt += 1
print(cnt)