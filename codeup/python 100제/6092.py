# 같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는,
# 방문 주기가 공백을 두고 입력된다. (단, 입력값은 100이하의 자연수이다.)

n = int(input())
num_list = list(map(int, input().split()))
count_list = []

for i in range(1, 24):
    count_list.append(0)
# count_list에 일단 디폴트 값인 0을 넣음
# 번호가 1부터 23까지니까 range(1, 24)

for i in num_list:
    count_list[i - 1] += 1

for i in count_list:
    print(i, end = ' ')







