import sys
input = sys.stdin.readline

K, L = map(int, input().split())

sugang = {}
for i in range(L):
    data = input().rstrip()
    # 이전에 딕셔너리에 있던 키가 들어오면 그대로 값이 업데이트
    sugang[data] = i
        
answer = sorted(sugang.items(), key = lambda x : x[1])

# 뽑는 횟수 K 보다 answer 요소 개수가 작으면 indexError 발생하므로 예외 처리
if len(answer) < K:
    for j in range(len(answer)):
        print(answer[j][0])
else:
    for j in range(K):
        print(answer[j][0])