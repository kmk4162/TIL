N = int(input()) # 얘는 고정, 비교를 계속 해야하니까
num = N
cnt = 0

while True:
    A = num // 10
    B = num % 10
    var_1 = A + B
    var_2 = num % 10
    var_3 = var_1 % 10
    num = var_2 * 10 + var_3
    cnt += 1
    if num == N:
        break
print(cnt)