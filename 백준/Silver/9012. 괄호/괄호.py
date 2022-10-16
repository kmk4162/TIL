from collections import deque
import sys
input = sys.stdin.readline

T= int(input())

for test in range(T):
    cnt = 0
    word = list(input())
    # 괄호 하나하나 담기
    for i in word:
        if cnt < 0 :
            break
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
    if cnt == 0:
        print('YES')
    else:
        print('NO')