N = int(input())

for i in range(1, N):
    stars = ' ' * (i - 1) + '*' * (((2 * N) - 1) - (2 * (i - 1)))
    print(stars)
print(' ' * (N - 1) + '*' * 1)

for i in range(1, N):
    stars = ' ' * (N - i - 1) + '*' * (2 * i + 1)
    print(stars)