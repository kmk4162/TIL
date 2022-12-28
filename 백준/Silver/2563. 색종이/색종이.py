import sys
input = sys.stdin.readline

N = int(input())
# 가로, 세로 10씩
white_board = [[0] * 101 for _ in range(101)]
for i in range(N):
    x, y = map(int, input().split())
    for row in range(x, x + 10):
        for col in range(y, y + 10):
            white_board[row][col] = 1
cnt = 0
for i in range(101):
    for j in range(101):
        if white_board[i][j] == 1:
            cnt += 1
print(cnt)