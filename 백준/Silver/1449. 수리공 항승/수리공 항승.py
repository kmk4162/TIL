import sys
input = sys.stdin.readline

N, L = map(int, input().split())
locations = sorted(list(map(int, input().split())))

answer = 0
start = locations[0]
for idx in range(len(locations)):
	# 처음은 패스
	if idx == 0:
		continue
	# a, b 좌표간의 테이프 길이는 (a - b + 1)	
	if locations[idx] - start + 1 > L:
		answer += 1
		start = locations[idx]
print(answer + 1)