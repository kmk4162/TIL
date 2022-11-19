for test_case in range(1, 11):
    N = int(input())
    graph = []
    for i in range(N):
        line = list(map(int, input().split()))
        graph.append(line)
    cnt = 0
    # 1이 N극, 2가 S극
    # 세로줄 탐색
    for j in range(N):
        # 줄 바뀔 때마다 초기화
        isN = False
        for i in range(N):
            if graph[i][j] == 1 and isN == False:
                isN = True
            elif graph[i][j] == 2 and isN == True:
                isN = False
                cnt += 1
    print(f'#{test_case}', cnt)