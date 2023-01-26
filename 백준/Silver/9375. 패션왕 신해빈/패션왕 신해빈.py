import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    clothes = {}
    N = int(input())
    for _ in range(N):
        item, category = input().split()
        clothes[category] = clothes.get(category, 0) + 1
    answer = []
    for k, v in clothes.items():
        answer.append(v)
    
    if len(answer) == 1:
        print(answer[0])
    else:
        cnt = 1
        for j in answer:
            cnt *= (j + 1)
        print(cnt - 1)