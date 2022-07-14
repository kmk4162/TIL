# 정수(1 ~ 100) 1개를 입력받아 
# 1부터 그 수까지 짝수의 합을 구해보자.

num = int(input())
cnt = 1
tot = 0

while cnt < num:
    cnt += 1
    if cnt % 2 == 0:
        tot += cnt
    continue
print(tot)