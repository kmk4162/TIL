import sys
input = sys.stdin.readline

A, P = map(int, input().split())
arr = []
arr.append(A)
def dfs(A):
    answer = 0
    for char in str(A):
        # P번 반복
        target_number = 1
        for i in range(P):
            target_number *= int(char)
        answer += target_number
    if answer in arr:
        arr.append(answer)
        return
    arr.append(answer)
    dfs(answer)
dfs(A)
cut_number = arr[-1]
result = []  
for i in arr:
    if i != cut_number:
        result.append(i)
    else:
        break
print(len(result))