import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
dp = [0] * 100001
visited = [False] * 100001

def check():
    if N == K:
        print(dp[N])
        return
    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()
        # 순간이동 먼저
        if 0 <= 2*x <= 100000 and not visited[2*x]:
            dp[2*x] = dp[x]
            visited[2*x] = True
            if 2*x == K:
                print(dp[2*x])
                return
            else:
                queue.appendleft(2*x)
        for i in (x - 1, x + 1):
            if 0 <= i <= 100000 and not visited[i]:
                dp[i] = dp[x] + 1
                visited[i] = True
                if i == K:
                    print(dp[i])
                    return
                else:
                    queue.append(i)
check()
