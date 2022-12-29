N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 10**9
answer = sum(arr)

while start <= end:
    # 블루레이 크기
    mid = (start + end) // 2
    if mid < max(arr):
        start = mid + 1
        continue
    cnt = 1 # 블루레이 개수
    sum_cnt = 0 # 합 카운트
    for i in arr:
        if sum_cnt + i <= mid:
            sum_cnt += i
        else:
            sum_cnt = i
            cnt += 1
    if cnt <= M:
        end = mid - 1
        answer = min(answer, mid)
    else:
        start = mid + 1
print(answer)