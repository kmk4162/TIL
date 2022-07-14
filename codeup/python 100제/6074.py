# 영문 소문자(a ~ z) 1개가 입력되었을 때,
# a부터 그 문자까지의 알파벳을 순서대로 출력해보자.
# 97 ~ 122
eng = input()
eng_to_num = ord(eng)
a = 97

while eng_to_num >= a:
    print(chr(a), end=' ')
    a += 1


