T = int(input())

for test_case in range(T):
    m, n = map(int, input().split())

    if m == 0:
        prize_m = 0
    elif m == 1:
        prize_m = 5000000
    elif m <= 3:
        prize_m = 3000000
    elif m <= 6:
        prize_m = 2000000
    elif m <= 10:
        prize_m = 500000
    elif m <= 15:
        prize_m = 300000
    elif m <= 21:
        prize_m = 100000
    else:
        prize_m = 0

    if n == 0:
        prize_n = 0
    elif n == 1:
        prize_n = 5120000
    elif n <= 3:
        prize_n = 2560000
    elif n <= 7:
        prize_n = 1280000
    elif n <= 15:
        prize_n = 640000
    elif n <= 31:
        prize_n = 320000
    else:
        prize_n = 0
    print(prize_m + prize_n)
