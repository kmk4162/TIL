# 1부터 n까지의 합을 구하여 출력하는 코드
#! sum() 함수 사용 금지

n = int(input())
cnt = 1
total = 0

# 1. while문

while cnt <=  n:
    total += cnt
    print(cnt, total)
    cnt += 1
print(f'총합은 {total} 입니다')

#2. for문

for i in range(n):
    total += cnt
    print(cnt, total)
    cnt += 1
print(f'총합은 {total} 입니다')