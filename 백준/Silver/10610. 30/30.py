import sys
input = sys.stdin.readline

n = list(map(str, sys.stdin.readline().strip()))
n.sort(reverse= True) # 가장 큰 수를 만들기 위해 내림차순으로 정렬
n = "".join(n) # 정렬한 수를 합쳐준다.

# 조건문을 통해 수가 30으로 나누어 떨어지면 수를 출력
if int(n) % 30 == 0:
    print(n)

# 나누어 떨어지지 않으면 -1 를 출력
else:
    print(-1)