import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = list(int(input()) for _ in range(K))
# print(lines)

# 만약 100 단위로 자르면
# 8, 7, 4, 5 -> 24개가 되니까 너무 잘게 자른것 -> 단위를 크게
start_line = 1
end_line = max(lines)
answer = 0
while start_line <= end_line:
    # mid가 자르는 단위
    mid = (start_line + end_line) // 2 # 정수니까 몫으로 계산
    line_cnt = 0
    for line in lines:
        line_cnt += line // mid
    if line_cnt < N:
        end_line = mid - 1
    else:
        answer = mid
        start_line = mid + 1
print(answer)