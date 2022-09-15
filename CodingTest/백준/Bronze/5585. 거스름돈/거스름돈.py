N = int(input())
cnt = 0
coins = [500, 100, 50, 10, 5, 1]
result = 1000 - N
for i in coins:
    x = result // i
    cnt += x
    result -= i * x
    if result == 0:
        break
print(cnt)