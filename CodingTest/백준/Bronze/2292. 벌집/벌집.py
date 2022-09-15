N = int(input())
cnt = 0
start = 1
while True:
    cnt += 1
    scope = 6 * cnt
    if N == 1:
        print(1)
        break
    if N <= start + scope:
        print(cnt + 1)
        break
    else:
        start += scope