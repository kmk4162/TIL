# 문자열 word가 주어질 때, 해당 문자열에서 
# a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
#! find() index() 메서드 사용 금지

#* 1. 문자열 자체를 순회
word = input()
cnt = 0

for i in word:
    if i == 'a':
        print(cnt)
        break
    else:
        cnt += 1
if cnt == len(word):
    print(-1)

#* 2. 문자열이 아니라 range와 index 이용
word = input()

for i in range(len(word)):
    if word[i] == 'a':
        print(i)
        break
else:
    print(-1)




