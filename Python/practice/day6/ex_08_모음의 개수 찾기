# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

#* Before

word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or "e" or "i" or "o" or "u":
        count += 1

print(count)

# 무슨 에러?
#! 에러 코드는 안 뜨지만 논리적 오류!
#! 3이 나와야하는데 12가 나옴

# 이유
# 모움일 때만 count가 올라가야 하는데 디버그 해보니 글자마다 다 올라감
#? char == "a" or "e" or "i" or "o" or "u" 의 뜻은 
#? `char이 a이거나 e거나 i거나 o거나 u이니?`가 아니라
#? a또는 e또는 i또는 o또는 u랑 같은 타입이니?를 뜻함
#? or 연산자는 bool 타입의 연산자이지 비교 연산자가 아님!!
#* ------------------------------------------------------------------------------

#* After

word = "HappyHacking"

count = 0
moeum = ['a', 'e', 'i', 'o', 'u']
#을 써서 char이 moeum 리스트 안에 들어가니?로 풀수도 있고

for char in word:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1

print(count)

