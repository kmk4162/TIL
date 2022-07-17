# 문자열 word가 주어질 때, Dictionary를 활용해서 
# 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

word = input()
my_dict = {}

#* 1. 문자열 자체 순회
# for i in word:
#     if i in my_dict:
#         my_dict[i] += 1
#     else:
#         my_dict[i] = 1

#* 2. 인덱스로 접근; 딕셔너리에서 쓰면 word[i]는 문자열의 i번째 문자, my_dict[word[i]] 는 그 i번째 문자를 key로 하는 value가 됨!       
# for i in range(len(word)):
#     if word[i] not in my_dict:
#         my_dict[word[i]] = 1
#     else:
#         my_dict[word[i]] += 1

#* 3. get 메서드; word[i]라는 key의 value를 가져오고, key가 존재하지 않는다면 word[i] 뒤에 설정해둔 0이라는 값으로 설정
#* 그 다움에 +1를 해주면, 처음 나오는 key는 0 + 1 = 1이 될 것이고, 이미 존재하는 key라면 (이미 2번 나왔었다면) 2 + 1 = 3 으로 업데이트!
for i in range(len(word)):
    my_dict[word[i]] = my_dict.get(word[i], 0) + 1

for i in my_dict:
    print(f'{i} {my_dict[i]}')
    # print(i, my_dict[i]) 가 더 간단!
