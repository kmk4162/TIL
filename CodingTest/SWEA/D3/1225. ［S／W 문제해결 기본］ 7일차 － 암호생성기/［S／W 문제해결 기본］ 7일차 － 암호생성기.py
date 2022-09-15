for test_case in range(10):
    T = int(input())
    list_ = list(map(int, input().split())) 
    while list_[-1] != 0:
        for i in range(1, 6):
            x = list_.pop(0)
            list_.append(x)
            list_[-1] -= i
            if list_[-1] <= 0:
                list_[-1] = 0
                break
    print(f'#{test_case + 1}', end = ' ')
    for i in list_:
        print(i, end = ' ')
    print()