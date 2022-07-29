T = int(input())

for i in range(T):
    test_case = int(input())
    moneys = list(map(int, input().split()))
    avg = float(sum(moneys) / len(moneys))
    cnt = 0
    for j in moneys:
        if j <= avg:
            cnt += 1
    print(f'#{i + 1} {cnt}')