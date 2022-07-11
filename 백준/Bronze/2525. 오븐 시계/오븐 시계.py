h, m = map(int, input().split())
cooktime = int(input())

if m + cooktime >= 60:
    add_h = (m + cooktime) // 60
    m = (m + cooktime) % 60
    if h + add_h >= 24:
        h = (h + add_h) % 24
    else:
        h = h + add_h
else:
    m = m + cooktime

print(h, m)

