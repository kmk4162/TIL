# 1부터 n까지의 곱을 구하여 출력하는 코드를 
# 1) while 문 2) for 문으로 각각 작성하시오.

#1 while문
n = int(input())
cnt = 1
total = 1

while cnt <=  n:
    total *= cnt
    print(cnt, total)
    cnt += 1
print(f'총합은 {total} 입니다')

#2 for문
n = int(input())
cnt = 1
total = 1

for i in range(n):
    total *= cnt
    print(cnt, total)
    cnt += 1
print(f'총합은 {total} 입니다')