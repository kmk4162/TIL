import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))

cnt = 0
idx = N
while True:
    # 시작 인덱스
    idx -= 1
    if K // coins[idx] != 0:
        cnt += (K // coins[idx])
        K -= coins[idx] * (K // coins[idx])
    if K == 0:
        break
print(cnt)