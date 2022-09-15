A, B = map(int, input().split())
cnt = 0
# 4 42
while True:
    if B == A:
        cnt += 1
        break
    if A > B:
        break
    elif B % 2 == 0:
        cnt += 1
        B /= 2
        continue
    elif B % 10 == 1:
        cnt += 1
        B = B // 10
        continue
    else:
        break
if A != B:
    print(-1)
else:
    print(cnt)
 
# BFS 풀이
from collections import deque

A, B = map(int, input().split())
# A에서 B까지
# 연산 최솟값에 +1 출력, 못 만들면 -1
# 100, 40021 경우

def bfs(A, B):
    queue = deque([(A, 1)])
    while queue:
        num, cnt = queue.popleft()
        if num == B:
            print(cnt)
            return

        for i in [num * 2, num * 10 + 1]:
            if 1 <= i <= 1e9 and A <= i:
                queue.append((i, cnt+1))
    print(-1)
bfs(A, B)
