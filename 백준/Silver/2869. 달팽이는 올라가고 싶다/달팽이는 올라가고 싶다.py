a, b, v = map(int,input().split())
day = 1
if v == a:
    print(day)
else:
    x = v - a
    plusday = x // (a - b)
    if x % (a - b) != 0:
        plusday += 1
    # a - b가 x 보다 이미 커서 몫이 0인 경우 고려
    if plusday == 0:
        plusday += 1
    print(day + plusday)