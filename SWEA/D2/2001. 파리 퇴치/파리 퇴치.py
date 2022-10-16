T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())
    flylist = []
    for i in range(N):
        flylist.append(list(map(int, input().split())))
    # M 크기에 있는 파리 개수 넣는 리스트
    scorelist = []
    for i in range(N - M + 1):
        for j in range(N - M + 1): # i, j는 시작하는 위치
            result = 0
            for row in range(i, i + M):
                for col in range(j, j + M):
                    result += flylist[row][col]
            scorelist.append(result)
            # print(scorelist)
    print(f'#{test_case + 1}', max(scorelist))
