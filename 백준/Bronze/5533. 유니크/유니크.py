from pprint import *
import sys
input = sys.stdin.readline
# 전체 입력 받기
scores = []
people = int(input())
for i in range(people):
    x = list(map(int, input().split()))
    scores.append(x)
# 90도 돌려서 생각하기
new_scores = []
for row in range(3):
    cols = []
    for col in range(people):
        cols.append(scores[col][row])
    new_scores.append(cols)

# 점수 비교 : count해서 1개만 있으면 그대로 점수 추가하고
# 2개 이상 있으면 그대로 0점
default_scores = [0] * people
for row in range(3):
    for col in range(people):
        score = new_scores[row][col]
        if new_scores[row].count(score) == 1:
            default_scores[col] += score
for score in default_scores:
    print(score)
