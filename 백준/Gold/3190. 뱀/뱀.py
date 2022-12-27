import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
apple_graph = [[False] * N for _ in range(N)] # 사과 있는 보드
a = int(input())
if a != 0:
    for i in range(a):
        x, y = map(int, input().split())
        apple_graph[x - 1][y - 1] = True

# 방향 전환 딕셔너리
cmd_dict = {}
for i in range(int(input())):
    second, direction = input().split()
    cmd_dict[int(second)] = direction

# 종료가 되는지 아닌지
def move(x, y, d):
    global head_x, head_y 
    new_x = x + dx[d]
    new_y = y + dy[d]
    head_x = new_x
    head_y = new_y
    # 범위가 벗어나거나 몸통에 부딪히면 종료
    if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N or (new_x, new_y) in snake:
        return False
    else:
        # 사과가 있으면 꼬리 그대로에 머리만 늘어남
        if apple_graph[new_x][new_y] == True:
            apple_graph[new_x][new_y] = False
            snake.append((new_x, new_y))
        # 사과 없으면 끝 좌표(꼬리)를 빼주고 머리쪽을 추가
        else:
            snake.popleft()
            snake.append((new_x, new_y))
        return True

def change_left(d):
    if d == 0:
        d = 3
    elif d == 1:
        d = 0
    elif d == 2:
        d = 1
    else:
        d = 2
    return d

def change_right(d):
    if d == 0:
        d = 1
    elif d == 1:
        d = 2
    elif d == 2:
        d = 3
    else:
        d = 0
    return d

cnt = 0
# 초기 방향은 (0, 1)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction_index = 1 # 방향 인덱스

# 머리 좌표
head_x = 0
head_y = 0
snake = deque()
snake.append((head_x, head_y))
while True:
    cnt += 1
    result = move(head_x, head_y, direction_index)
    if cnt in cmd_dict:
        if cmd_dict[cnt] == 'L':
            direction_index = change_left(direction_index)
        else:
            direction_index = change_right(direction_index)
    if result == False:
        break
    # print(cnt, '초')
    # pprint(snake)
    # print('-------------------')
print(cnt)