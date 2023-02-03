import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr_1 = list(input().strip())
arr_2 = list(input().strip())
T = int(input())

team_1 = []
team_2 = []
for i in arr_1:
    team_1.append(i)
for i in arr_2:
    team_2.append(i)

arr_1.reverse()
arr = arr_1 + arr_2

cnt = 0
while cnt < T:
    cnt += 1
    for i in range(N + M - 1):
        if arr[i] in team_1 and arr[i + 1] in team_2:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            if arr[i + 1] == arr_1[-1]:
                break
print(''.join(arr))