T = int(input())

for test_case in range(T):
    a, b, c = map(int, input().split())
    if a == b == c:
        d = a
    elif a == b and a != c:
        d = c
    elif a == c and a != b:
        d = b
    elif b == c and a != b:
        d = a
    print(f'#{test_case + 1} {d}')
# a, b, c가 다 같다면 정사각형 이므로 d도 나머지 값들 따라감
# 직사각형은 두쌍씩 같을수 밖에 없고, a, b, c 중 2개만 같다면
# 나머지 한 변의 길이는 3개 중 다른 값 하나를 따라갈 수 밖에 없음