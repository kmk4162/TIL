N, M = map(int, input().split())

answer = []
def dfs():
    if len(answer) == M:
        print(*answer)
        return
    
    for i in range(1, N + 1):
        if len(answer) == 0:
            answer.append(i)
            dfs()
            answer.pop()
        else:
            if i not in answer and i > answer[-1]:
                answer.append(i)
                dfs()
                answer.pop()
dfs()