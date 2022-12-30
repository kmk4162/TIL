import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = []
def dfs():
    if len(answer) == M:
        print(*answer)
        return
    
    for i in arr:
        if len(answer) == 0:
            answer.append(i)
            dfs()
            answer.pop()
        elif len(answer) != 0 and i not in answer:
            answer.append(i)
            dfs()
            answer.pop()
dfs()