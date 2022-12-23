import sys
input = sys.stdin.readline

S = int(input())
result = 0
cnt = 0
while True:
    cnt += 1
    result += cnt
    # print(result)
    if S < result:
        cnt -= 1
        break
    elif S == result:
        break 
print(cnt)