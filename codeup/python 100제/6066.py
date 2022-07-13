# 3개의 정수(a, b, c)가 입력되었을 때
# 짝(even)/홀(odd)을 출력해보자.

list1 = list(map(int, input().split()))

for i in list1:
    if i % 2 == 0:
        print('even')
    else:
        print('odd')




