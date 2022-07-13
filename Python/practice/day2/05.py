# 주어진 숫자의 평균을 구하는 코드를 작성하시오.
# sum(), len()  함수 사용 금지

numbers = [3, 10, 20]
cnt = 0
num_sum = 0

for i in numbers:
    num_sum += i
    print(num_sum)
    cnt += 1
print(f'평균은 {num_sum / cnt} 입니다!')