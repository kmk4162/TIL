# 출석을 부른 번호 중에 가장 빠른 번호를 출력한다.
#! 첫 번째 번호와 마지막 번호가 몇 번인지는 아무도 모른다.
#! 음수(-) 번호, 0번 번호도 있을 수 있다.

n = int(input())
num_list = list(map(int, input().split()))

#* 1. 메서드 쓰고 풀기
# print(min(num_list))

#* 2. 메서드 안 쓰고 알고리즘으로 풀기
small = num_list[0]
for i in num_list:
    if i <= small:
        small = i
print(small)







