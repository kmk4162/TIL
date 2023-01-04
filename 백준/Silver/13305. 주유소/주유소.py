N = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

min_oil = oil[0]
money = 0
for i in range(N - 1):
    if oil[i] > min_oil:
        money += min_oil * road[i]
    else:
        money += oil[i] * road[i]
        min_oil = oil[i]
print(money)