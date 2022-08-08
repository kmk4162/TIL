import sys
input = sys.stdin.readline

N, M = map(int, input().split())

cardlist = list(map(int, input().split()))
# 처음부터 정렬
cardlist. sort()
blackjack = []

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            result = cardlist[i] + cardlist[j] + cardlist[k]
            if result > M:
                break
            blackjack.append(result)
print(sorted(blackjack)[-1])