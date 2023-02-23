import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(0)
arr.append(L)
arr.sort()

# 휴게소 사이의 길이를 이분탐색
start = 1
end = L - 1
answer = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] > mid:
            cnt += (arr[i] - arr[i - 1] - 1) // mid
    
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid
print(answer)