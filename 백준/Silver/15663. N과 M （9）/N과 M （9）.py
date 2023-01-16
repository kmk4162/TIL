import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = []
visited = [False] * N
def dfs():
    prev = 0
    if len(answer) == M:
        print(*answer)
        return
    
    for i in range(N):
        if arr[i] != prev and visited[i] == False:
            answer.append(arr[i])
            prev = arr[i]
            visited[i] = True
            dfs()
            answer.pop()
            visited[i] = False
dfs()