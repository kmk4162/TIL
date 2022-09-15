# 번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
# n개의 랜덤 번호(k, 1 ~ 23)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.
# 출석 부른 번호 순서를 바꿔서 공백을 두고 출력

#* 1. 메서드 쓰고 풀기
n = int(input())
num_list = list(map(int, input().split()))
num_list.reverse()

for i in num_list:
    print(i, end = " ")

#* 2. 슬라이싱으로 풀기
n = int(input())
num_list = list(map(int, input().split()))
for i in num_list[::-1]:
    print(i, end = " ")







