# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

n = int(input())

while True:
    n = n - 1
    if n != 0:
        print(n)
    else:
        print(0)
        break

