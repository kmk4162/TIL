import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [False] * N
answer = []

def dfs(idx):
    if len(answer) == M:
        print(*answer)
        return
    
    prev = 0
    for i in range(idx + 1, N):
        if arr[i] != prev and visited[i] == False:
            answer.append(arr[i])
            visited[i] = True
            prev = arr[i]
            dfs(i)
            answer.pop()
            visited[i] = False

dfs(-1)