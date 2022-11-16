T = int(input())
for test_case in range(T):
    N, Q = map(int, input().split())
    boxes = [0] * N
    # Q번 반복
    for i in range(1, Q + 1):
        # L, R은 범위
        L, R = map(int, input().split())
        for j in range(L, R + 1):
            boxes[j - 1] = i
    print(f'#{test_case + 1}', * boxes)