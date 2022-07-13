# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지
numbers = [0, 20, 100]
biggest = numbers[0]

for i in numbers:
    if i > biggest:
        biggest = i
    print(f'현재까지 가장 큰 수는 {biggest} 입니다!')

print(f'따라서 가장 큰 수는 {biggest} 입니다!')

# numbers를 for문 돌리면서

# 현재까지 가장 큰 숫자 ⇒ biggest 변수 만들고

# 다음 변수랑 비교해서(if문 이용), 기존 변수에 비해 작으면 그대로두고 크면 교체한다

# 비교 숫자를 그냥 0으로 두니까 마이너스나 다른 테스트 케이스에선 안 먹힘

# 그래서 초기 biggest를 0이 아니라 입력한 numbers의 첫번째 요소인 numbers[0]으로 설정!