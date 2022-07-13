# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.

num = list(map(int, input().split()))

for i in num:
    while True:
        if num == 0:
            break
print(num)



