T = int(input())

for test_case in range(T):
    numbers = []
    count = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{test_case + 1}', *sorted(numbers))
    