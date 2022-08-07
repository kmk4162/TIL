T = int(input())
moneys = [0] * 8
for test_case in range(T):
    money = int(input())
    for i in range(8):
        # 50000, 5000, 500, 50 일때
        if i % 2 == 0:
            divcnt = 50000 / (10 ** (i * 0.5))
            moneys[i] = int(money // divcnt)
            money -= moneys[i] * divcnt
        # 10000, 1000, 100, 10 일때
        else:
            divcnt = 10000 / (10 ** ((i * 0.5) - 0.5))
            moneys[i] = int(money // divcnt)
            money -= moneys[i] * divcnt
    print(f'#{test_case + 1}')
    print(*moneys)