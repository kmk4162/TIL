A, B, C = map(int, input().split())
# 전체 시간은 1 ~ 100
alltimes = [0] * 100

for i in range(3):
    s, e = map(int, input().split())
    for j in range(s, e):
        alltimes[j] += 1
money_A = alltimes.count(1) * A
money_B = alltimes.count(2) * B * 2
money_C = alltimes.count(3) * C * 3
print(money_A + money_B + money_C)