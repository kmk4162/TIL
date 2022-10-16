M = int(input())
cnt = 1
for i in range(M):
    cups = list(map(int, input().split()))
    if cnt in cups:
        cups.remove(cnt)
        cnt = cups[0]
    else:
        continue
print(cnt)