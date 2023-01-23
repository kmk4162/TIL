N = int(input())
def dfs(N):
    cnt = 0
    while N > 0:
        if N % 5 != 0:
            N -= 2
            cnt += 1
        else:
            N -= 5
            cnt += 1
    return (cnt, N)
answer = dfs(N)
if answer[1] < 0:
    print(-1)
else:
    print(answer[0])