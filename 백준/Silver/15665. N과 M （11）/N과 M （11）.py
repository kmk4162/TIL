import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(list(set(arr)))

answer = []
def dfs():
    if len(answer) == M:
        print(*answer)
        return
    
    for i in range(len(arr)):
        answer.append(arr[i])
        dfs()
        answer.pop()
    
dfs()