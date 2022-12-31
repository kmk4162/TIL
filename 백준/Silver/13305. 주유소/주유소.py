import sys
input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

price = road[0] * oil[0] # 첫번째 가격

# 가장 값이 싼 주유소
min_oil = oil[0]
for i in range(1, N - 1):
    if min_oil > oil[i]:
        min_oil = oil[i]
    price += min_oil * road[i]
print(price)