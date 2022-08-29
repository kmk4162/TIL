A, B = map(int, input().split())
cnt = 0
# 4 42
while True:
    if B == A:
        cnt += 1
        break
    if A > B:
        break
    elif B % 2 == 0:
        cnt += 1
        B /= 2
        continue
    elif B % 10 == 1:
        cnt += 1
        B = B // 10
        continue
    else:
        break
if A != B:
    print(-1)
else:
    print(cnt)