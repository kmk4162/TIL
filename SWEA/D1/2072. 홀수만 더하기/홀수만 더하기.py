T = int(input())
for i in range(1, T + 1):
    result = 0
    num_list = list(map(int, input().split()))
    for num in num_list:
        if num % 2 == 1:
            result += num
    print(f'#{i} {result}')