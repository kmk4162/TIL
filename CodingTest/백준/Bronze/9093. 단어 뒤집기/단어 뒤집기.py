T = int(input())

for test_case in range(T):
    words = list(input().split())
    for word in words:
        print(word[::-1], end = ' ')
    print()