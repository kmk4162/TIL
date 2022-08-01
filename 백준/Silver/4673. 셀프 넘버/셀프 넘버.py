cnt = 0
digit_sum = 0
result = 0
gen_list = []

# 생성자들이 있는 수만 모은 리스트 만들기
while cnt <= 10000:
    cnt += 1
    digit_sum = sum(list(map(int, str(cnt))))
    result = cnt + digit_sum
    gen_list.append(result)

B = set(sorted(gen_list))
whole_list = set(range(1, 10001))
# 1부터 10000까지 있는 whole_list에 B를 빼는 차집합 연산
# set으로 바꿔서 연산
self_numbers = whole_list - B
for i in sorted(self_numbers):
    print(i)