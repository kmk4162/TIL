listen, see = map(int, input().split())
no_dict = {}

for i in range(listen):
    x = input()
    no_dict[x] = 1
for i in range(see):
    x = input()
    no_dict[x] = no_dict.get(x, 0) + 1  
# value가 2인 것들만 모으면 듣보잡만 출력 가능
no_dict_sort = sorted(no_dict.items(), key = lambda x : (-x[1], x[0]))
print(listen + see - len(no_dict))
# 듣보잡 수는 listen + see에 중복을 제외한 숫자를 빼주면
# 순수 중복되는 듣보잡 수만 구할 수 있음
for i in no_dict_sort:
    if i[1] == 2:
        print(i[0])



