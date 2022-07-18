# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

#* Before

N = 10
answer = ()
for number in range(N + 1):
    answer.append(number * 2)

print(answer)

# 무슨 에러?
#! AttributeError: 'tuple' object has no attribute 'append'

# 이유
# tuple에는 append를 사용할 수 없음
# list로 바꿔야함
#* ------------------------------------------------------------------------------

#* After

N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)
