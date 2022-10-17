def solution(n):
    answer = 0
    cnt = 0
    while True:
        if n == 0:
            break
        cnt += 1
        if n % cnt == 0:
            answer += (n // cnt)
        if cnt == n:
            break
    return answer