import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for i in range(T):
    cmd = input().strip()
    n = int(input())
    s = input().replace('[','').replace(']','').strip()
    if n == 0:
        s = []
    else:
        s = list(map(int, s.split(',')))
    word = deque(s)

    flag = False
    reverse_cnt = 0
    for d in cmd:
        if d == 'R':
            reverse_cnt += 1
        else:
            # D 실행
            if len(word) != 0:
                if reverse_cnt % 2 == 1:
                    word.pop()
                else:
                    word.popleft()
            else:
                print('error')
                flag = True
                break
    if not flag:
        word = list(word)
        if reverse_cnt % 2 == 1:
            word.reverse()
        answer = ''
        for i in word:
            answer += str(i)
            answer += ','
        answer = answer[:-1]
        print('[' + answer + ']')