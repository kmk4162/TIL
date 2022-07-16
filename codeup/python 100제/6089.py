# 시작 값(a), 등비의 값(r), 몇 번째 인지를 나타내는 정수(n)가
# 공백을 두고 입력된다.(모두 0 ~ 10)

a, r, n = map(int, input().split())

x = a * r ** (n - 1)
print(x)


