# 1부터 n까지의 곱을 구하여 출력하는 코드

n = int(input())
cnt = 1
total = 1

#* 1. while문

while cnt <=  n:
    total *= cnt
    print(cnt, total)
    cnt += 1
print(f'총합은 {total} 입니다')

#* 1-1. while + if문
#? 내가 생각해서 작성했는데 이게 좋은 코드인지는 모르겠다
#todo 시간복잡도? 그 개념을 적용했을 때 1-1은 1보다 안 좋은 코드인지 확인해보자!

while True:
    if cnt <= n:
        total *= cnt
        print(cnt, total)
        cnt += 1
    else:
        break
print(f'총합은 {total} 입니다')

#2*. for문

for i in range(n):
    total *= cnt
    print(cnt, total)
    cnt += 1
print(f'총합은 {total} 입니다')