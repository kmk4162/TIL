while True:
    list_ = list(map(int, input().split()))
    if list_.count(0) == 3:
        break 
    list_.sort()
    if list_[0] ** 2 + list_[1] ** 2 == list_[2] ** 2:
        print('right')
    else:
        print('wrong')