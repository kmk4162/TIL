N = int(input())

for i in range(1, N):
    stars = ' ' * (N - i) + '*' * i
    print(stars)
print('*' * N)
for i in range(1, N):
    stars = ' ' * i + '*' * (N - i) 
    print(stars)