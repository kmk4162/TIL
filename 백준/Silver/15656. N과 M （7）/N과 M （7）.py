N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = []

def dfs():
    if len(answer) == M:
        print(*answer)
        return
    for i in range(N):
        for j in range(N):
            answer.append(arr[i])
            dfs()
            answer.pop()
            break
dfs()