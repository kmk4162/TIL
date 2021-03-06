# 아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

#* Before

from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count = {fruit: 1}
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)

# 무슨 에러?
#! 에러 코드는 안 뜨지만 논리적 오류!
#! 전체가 안 나오고 리스트의 마지막 요소인 {'Salal berry': 1}만 카운트 하고 반환

# 이유
# fruit_count에 없는 과일(key)은 추가를 해야하는데 23번 코드는 추가가 아니고 덮어쓰기만 계속 함
# fruit_count가 아니라 fruit_count의 key에 접근을 해야함!
#* ------------------------------------------------------------------------------

#* After

from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)


