N = int(input())
cnt = 2
result = 0
while True:
    if N % cnt == 0:
        N /= cnt
        print(cnt)
        continue
    else:
        cnt += 1
    if N == 1:
        break  