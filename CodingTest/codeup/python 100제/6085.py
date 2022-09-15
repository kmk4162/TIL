# w, h, b 가 공백을 두고 입력된다.
# 이미지 저장 용량 공식 = w * h * b / 8 / 1024 / 1024
# 소수 둘째 자리까지의 정확도(반올림)

w, h, b = map(int, input().split())

bit = w * h * b / 8 / 1024 / 1024
print("{:.2f}".format(bit), 'MB')
