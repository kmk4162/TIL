C = int(input())
for test_case in range(C):
    numbers = list(map(int, input().split()))
    N = numbers[0]
    avg = sum(numbers[1:]) / N
    cnt = 0
    for num in numbers[1:]:
        if num > avg:
            cnt += 1
    # 퍼센트 계산 위해 곱하기 100
    result = (cnt / N) * 100
    print(format(result, '.3f') + '%')