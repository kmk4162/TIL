# 분할 정복 문제
A, B, C = map(int, input().split())

def multiple(x, y, z):
    if y == 1:
        return x % z
    else:
        temp = multiple(x, y // 2, z)
        if y % 2 == 0: # 짝수
            return (temp * temp) % z
        else: # 홀수
            return (temp * temp * x) % z

print(multiple(A, B, C))