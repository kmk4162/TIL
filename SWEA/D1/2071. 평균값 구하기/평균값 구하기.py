T = int(input())
for i in range(T):
    list1 = list(map(int, input().split()))
    sum1 = sum(list1)
    avg = round(sum1 / 10)
    print(f'#{i}', avg)