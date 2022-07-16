# A, B, C, D, E, F 중 하나가 입력될 때,
# 1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
# (단, A ~ F 까지만 입력된다.)

num = int(input(), 16)

for i in range(1, 16):
    a = num * i
    print(f"{'%X'%num}*{'%X'%i}={'%X'%a}")