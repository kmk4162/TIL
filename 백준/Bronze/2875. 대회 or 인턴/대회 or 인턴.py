import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
cnt = 0
while True:
    if n - 2 >= 0 and m - 1 >= 0:
        if n + m -3 >= k:
            n -= 2
            m -= 1
            cnt += 1
        else:
            break
    else:
        break
print(cnt)