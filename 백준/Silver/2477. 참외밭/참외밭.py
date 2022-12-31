import sys
input = sys.stdin.readline

N = int(input())
cmd = []
cmd_dict = {}
for i in range(6):
    direction, length = map(int, input().split())
    cmd.append((direction, length))
    cmd_dict[direction] = cmd_dict.get(direction, 0) + 1

large_index_list = []
for i in range(len(cmd)):
    if cmd_dict[cmd[i][0]] == 1:
        large_index_list.append(i)

# 큰 사각형 구하기
big_square = 1
for i in large_index_list:
    big_square *= cmd[i][1]

# 작은 사각형 구하기
small_square = 1
indexs = large_index_list.copy()
for i in large_index_list:
    if i == 0:
        indexs.append(5)
    else:
        indexs.append(i - 1)
    indexs.append((i + 1) % 6)
small_indexs = set(range(0, 6)) - (set(indexs))
for i in list(small_indexs):
    small_square *= cmd[i][1]

print((big_square - small_square) * N)