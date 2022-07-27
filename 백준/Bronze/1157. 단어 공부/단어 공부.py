word = input()
word = word.upper()
word_dict = {}

for i in word:
    word_dict[i] = word_dict.get(i, 0) + 1
# 딕셔너리에 알파벳 등장 횟수 업데이트

max_cnt = max(word_dict.values())
# 일단 제일 큰 수를 변수에 담기
max_list = []
# 제일 큰 수와 같은 값들을 리스트에 추가
for i in word_dict:
    if word_dict[i] == max_cnt:
        max_list.append(i)

if len(max_list) == 1:
    print(max_list[0])
else:
    print('?')
# 큰 값이 기본 1개이니까 길이가 1이라면 그대로 출력
# max_list에 2개 이상이 존재한다면 가장 많이 출력된 알파벳이 여러개 있다는
# 뜻이므로 ? 출력
