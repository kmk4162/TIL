A, B = map(int, input().split())
cnt = 1
while True:
    cnt += 1
    if int(str(B)[-1]) == 1:
        B = int(str(B)[:-1])
    else:
        if B % 2 == 0:
            B //= 2
        else:
            cnt = -1
            break
    if B == A:
        break
    if B < A:
        cnt = -1
        break
print(cnt)