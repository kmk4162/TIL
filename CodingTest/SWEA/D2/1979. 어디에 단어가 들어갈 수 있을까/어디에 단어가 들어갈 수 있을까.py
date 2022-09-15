T = int(input())

for test_case in range(T):
    cnt_tot = 0
    N, K = map(int, input().split())
    wordlist = []
    for i in range(N):
        x = list(input().split())
        wordlist.append(x)

    for i in wordlist:
        cnt_good = 0
        x = ''.join(i)
        linelist = []
        for char in x:
            if char == '1':
                cnt_good += 1
            else:
                linelist.append(cnt_good)
                cnt_good = 0
        linelist.append(cnt_good)
        cnt_tot += linelist.count(K)
        # 한 줄 안에 cnt_good이 여러개 존재할 수 있는데
        # 그 중에서 K 길이 인것만 카운트

    new_wordlist = []
    for j in range(N):
        col = []
        for i in range(N):
            col.append(wordlist[i][j])
        new_wordlist.append(col)

    for i in new_wordlist:
        cnt_good = 0
        x = ''.join(i)
        linelist = []
        for char in x:
            if char == '1':
                cnt_good += 1
            else:
                linelist.append(cnt_good)
                cnt_good = 0
        linelist.append(cnt_good)
        cnt_tot += linelist.count(K)
    print(f'#{test_case + 1}', cnt_tot)