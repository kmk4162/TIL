# 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
#! min() 함수 사용 금지

numbers = [0, 20, 100]
smallest = numbers[0]

for i in numbers:
    if i < smallest:
        smallest = i
    print(f'현재까지 가장 작은 수는 {smallest} 입니다!')

print(f'따라서 가장 작은 수는 {smallest} 입니다!')
