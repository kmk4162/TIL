import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(list(set(arr)))

answer = []
def dfs(now_num):
    if len(answer) == M:
        print(*answer)
        return
    for i in range(len(arr)):
        if arr[i] >= now_num:
            answer.append(arr[i])
            now_num = arr[i]
            dfs(now_num)
            answer.pop()
dfs(0)