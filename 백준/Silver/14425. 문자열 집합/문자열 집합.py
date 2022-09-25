N, M = map(int, input().split())

dictS = {}
for word in range(N):
    dictS[input()] = 1

cnt = 0
for _ in range(M):
    check = input()
    if check in dictS:
        cnt += 1
print(cnt)