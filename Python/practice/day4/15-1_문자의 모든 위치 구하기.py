# 문자열 word가 주어질 때, 해당 문자열에서 
# a 의 모든 위치(index)를 출력해주세요.
#! find() index() 메서드 사용 금지

#* 1. 문자열 자체 순회
word = input()
cnt = 0

for i in word:
    if i == 'a':
        print(cnt)
        cnt += 1
    else:
        cnt += 1  

#* 2. 문자열 인덱스 접근법; 그때 그때 출력
word = input()

for i in range(len(word)):
    if word[i] == 'a':
        print(i, end = " ")

#* 3. 리스트에 담는 방법
word = input()
word_list = []

for i in range(len(word)):
    if word[i] == 'a':
        word_list.append(i)
x= map(str, word_list)
# join은 문자열만 가능, 지금 word_list의 요소들은 int형
# 따라서 map을 이용해서 word_list를 string으로 바꾸고 join을 써야함!
print(' '.join(x))
