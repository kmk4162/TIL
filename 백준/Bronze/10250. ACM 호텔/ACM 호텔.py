T = int(input())
for test_case in range(T):
    H, W, N = map(int, input().split())
    # 몇 층 인지, 나누어 떨어지면 전체 층 수 H
    floor = N % H
    if floor == 0:
        floor = H

    # 몇 호 인지
    roomnum = (N // H) + 1
    if N / H == int(N / H):
        roomnum -= 1
    print(floor * 100 + roomnum)