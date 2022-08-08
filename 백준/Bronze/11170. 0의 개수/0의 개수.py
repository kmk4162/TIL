T = int(input())

for testcase in range(T):
    cnt = 0
    N, M = map(int, input().split())
    for i in range(N, M + 1):
        cnt += str(i).count('0')
    print(cnt)
