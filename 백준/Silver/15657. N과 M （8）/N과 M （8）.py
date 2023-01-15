N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = []

def dfs(index):
    if len(answer) == M:
        print(*answer)
        return
    for i in range(index - 1, N):
        answer.append(arr[i])
        dfs(i + 1)
        answer.pop()
dfs(1)