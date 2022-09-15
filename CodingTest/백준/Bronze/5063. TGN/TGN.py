# r과 e - c 를 비교

num = int(input())

for i in range(num):
    r, e, c = map(int, input().split())
    if r > e - c:
        print('do not advertise')
    elif r < e - c:
        print('advertise')
    else:
        print('does not matter')