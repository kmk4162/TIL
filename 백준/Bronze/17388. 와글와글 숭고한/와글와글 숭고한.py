list_ = list(map(int, input().split()))
name = ['Soongsil', 'Korea', 'Hanyang']
if sum(list_) >= 100:
    print('OK')
else:
    x = list_.index(min(list_))
    print(name[x])