import sys
input = sys.stdin.readline

N = int(input())
datas = list(map(int, input().split()))
M = int(input())

start = 0
end = max(datas)
answer = 0
while start <= end:
    target = (start + end) // 2
    sum_cnt = 0
    for data in datas:
        if data > target:
            sum_cnt += target
        else:
            sum_cnt += data
    if sum_cnt > M:
        end = target - 1
    else:
        start = target + 1
        answer = target
if target > max(datas):
    print(max(datas))
else:
    print(answer)