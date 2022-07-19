T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    if a > b:
        x = '>' 
    elif a < b:
        x = '<'
    else:
        x = '='
    print(f'#{i + 1} {x}')