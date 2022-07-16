# 언제까지 합을 계산할 지, 정수 1개를 입력받는다.
# 1, 2, 3, 4, 5 ... 순서대로 계속 더해가다가
# 그 합이 입력된 정수보다 커지거나 같아지는 경우,
# 그때까지의 합을 출력한다.

n = int(input())
total = 0

for i in range(0, n + 1):
    if n == 0:
        break
    total += i
    if total >= n:
        break
print(total)
