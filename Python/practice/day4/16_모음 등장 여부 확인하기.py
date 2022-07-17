# 문자열 word가 주어질 때
# 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
#! count() 사용 금지

#* in 쓰기
word = input()
moeum = ['a', 'e', 'i', 'o', 'u']
cnt = 0

for i in word:
    if i in moeum:
        cnt += 1
print(cnt)
