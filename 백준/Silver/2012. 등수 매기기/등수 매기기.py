import sys
input = sys.stdin.readline

N = int(input())
scores = []
for i in range(N):
	scores.append(int(input()))
	
# 정렬하고 작은 순서대로 하나씩 빼면 됨
scores.sort()
answer = 0
for i in range(len(scores)):
	answer += abs(scores[i] - (i + 1))
print(answer)