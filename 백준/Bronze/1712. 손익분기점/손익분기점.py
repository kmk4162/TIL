A, B, C = map(int, input().split())
# A + B * 판매대수 < C * 판매대수가 돼야함
result = 0
if B >= C:
    result = -1
else:
    profit = C - B
    result = (A // profit) + 1
print(result)