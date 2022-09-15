# 가장 작은 수
a, b, c = map(int, input().split())

small1 = (b if a > b else a)
small2 = (small1 if c > small1 else c)
print(small2)