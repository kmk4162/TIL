# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

#* Before

words = list(map(int, input().split()))
print(words)

# 무슨 에러?
#! ValueError: invalid literal for int() with base 10: "I'm"


# 이유
# 문자열을 기준으로 나누려 하는데 int로 받아버리면 원하는 자료형이 아니라 에러가 발생
#* ------------------------------------------------------------------------------

#* After

words = list(map(str, input().split()))
print(words)
