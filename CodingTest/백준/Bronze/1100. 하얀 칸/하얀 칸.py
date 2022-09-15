import sys
from pprint import *
input = sys.stdin.readline

chess = []
for i in range(8):
    line = list(input().strip()) # 개행문자 제거
    chess.append(line)

# 하얀색은 x, y 좌표 더한 값이 짝수
cnt = 0
for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            if chess[row][col] == 'F':
                cnt += 1
print(cnt)