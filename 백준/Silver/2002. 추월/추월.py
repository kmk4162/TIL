import sys
input = sys.stdin.readline

# 입력 순서 그대로 출력이 나와야 함. 그렇지 않으면 추월한 것
cars = {}
N = int(input())
for i in range(N):
    car = input().rstrip()
    cars[car] = i + 1

# 나오는 차 순서 입력 받기
car_index_list = []
for i in range(N):
    car = input().rstrip()
    car_index_list.append(cars[car])

# 몇대가 추월했는지 파악하기
# (1, 2) (1, 3) (1, 4) (1, 5) (2, 3)... 선택해서 비교
# 앞의 숫자가 더 크다면 추월한 것으로 생각
answer = 0
for i in range(N):
    cnt = 0
    for j in range(i + 1, N):
        if car_index_list[i] > car_index_list[j]:
            cnt += 1
    if cnt != 0:
        answer += 1          
print(answer)