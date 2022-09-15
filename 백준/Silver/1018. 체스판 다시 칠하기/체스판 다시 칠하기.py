from pprint import pprint
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
chess = []
for i in range(N):
    line = list(map(str, input().rstrip()))
    chess.append(line)

chess_white = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

chess_black = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

def check_white(row, col):
    cnt = 0
    for i in range(row, row + 8):
            for j in range(col, col + 8):
                if chess[i][j] != chess_white[i-row][j-col]:
                    cnt += 1
    countlist.append(cnt)

def check_black(row, col):
    cnt = 0
    for i in range(row, row + 8):
            for j in range(col, col + 8):
                if chess[i][j] != chess_black[i-row][j-col]:
                    cnt += 1
    countlist.append(cnt)
                
# 각 시작점 마다의 바꾸는 횟수(cnt)를 저장하는 리스트
countlist = []

# 시작 지점 체크
for row in range(0, N - 7):
    for col in range(0, M - 7):
        check_white(row, col)
        check_black(row, col)
print(min(countlist))