N = int(input())
starA = ' *'
starB = '* '
for i in range(1, N + 1):
    maxline = N
    x = ' ' * (N - i) + '* ' * i
    print(x.rstrip())