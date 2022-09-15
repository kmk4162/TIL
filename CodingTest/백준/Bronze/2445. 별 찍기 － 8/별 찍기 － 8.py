N = int(input())

for i in range(1, N):
    stars = '*' * i +  ' ' * (2 * N - 2 * i) + '*' * i
    print(stars)
print('*' * (2 * N))

for i in range(1, N):
    stars = '*' * (N - i) +  ' ' * (2 * i) + '*' * (N - i)
    print(stars)