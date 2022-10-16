T = int(input())

for test_case in range(T):
    numbers = list(map(int, input().split()))
    numbers = sorted(numbers)
    print(numbers[-3])