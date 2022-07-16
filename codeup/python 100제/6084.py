# h, b, c, s 가 공백을 두고 입력된다.
# 저장 용량 공식 = h * b * c * s / 8 / 1024 / 1024
# 소수 첫째 자리까지의 정확도(반올림)

h, b, c, s = map(int, input().split())

bit = h * b * c * s / 8 / 1024 / 1024
print(round(bit, 1), 'MB')
