# 주어진 문자열 word가 주어질 때
# 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

#* 1. 내 방법; 조건 따라 리스트에 추가하고 join 쓰기
from hashlib import new

word = input()
changed_word=[]

for i in word:
    if i != 'a':
        changed_word.append(i)
print(''.join(changed_word))


#* 2. 강사님 풀이; 빈 문자열에 계속 추가하는 방법
word = input()
result = ''

for i in word:
    if i != 'a':
        result += i
        # result도 문자열이고, i도 문자열이니까 +로 붙이는게 가능
    print(result)
print(result)
