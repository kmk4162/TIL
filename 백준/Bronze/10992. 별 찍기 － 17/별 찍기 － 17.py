N = int(input())
if N == 1:
    print('*')
elif N == 2:
    print(' *')
    print('***')
else:
    for i in range(1, N + 1):
        if i != N:
            if i == 1:
                print(' ' * (N - 1) + '*')
                continue
            else:
                x = ' ' * (N - i) + '*' + ' ' * (2 * i - 3) + '*'
                print(x.rstrip())
        else:
            print('*' * (2 * N - 1))