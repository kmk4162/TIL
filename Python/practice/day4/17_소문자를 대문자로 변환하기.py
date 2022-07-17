# 소문자로 구성된 문자열 word가 주어질 때
# 모두 대문자로 바꾸어 표현하시오.
#! .upper(), .swapcase() 사용 금지

# 유니코드 변환 이용; 대문자와 소문자 사이 일정한 수 차이가 있음을 활용
word = input()

for i in word:
    new_word_num = ord(i) - 32
    new_word = chr(new_word_num)
    print(new_word, end ="")
