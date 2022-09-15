import sys
input = sys.stdin.readline

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 이기면 3점, 지면 그대로, 비기면 둘 다 1점씩
score_a = 0
score_b = 0
round_a = 0
round_b = 0
# A, B가 자신이 이겼던 라운드를 나타내는 변수

for round in range(10):
    if A[round] > B[round]:
        score_a += 3
        round_a = round + 1
    elif A[round] < B[round]:
        score_b += 3
        round_b = round + 1
    else:
        score_a += 1
        score_b += 1
print(score_a, score_b)
# 승자 출력
if score_a > score_b:
    print('A')
elif score_a < score_b:
    print('B')
elif score_a == score_b:
    if score_a == 10:
        print('D')
    else:
        print('A' if round_a > round_b else 'B')
