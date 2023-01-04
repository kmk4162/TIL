N = int(input())
cnt = 0
while True:
    if N % 5 != 0:
        N -= 3
        cnt += 1
    else:
        N -= 5
        cnt += 1
    if N == 0:
        break
    if N < 0:
        cnt = -1
        break
print(cnt)