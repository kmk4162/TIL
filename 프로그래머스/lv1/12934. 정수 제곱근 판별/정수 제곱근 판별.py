def solution(n):
    cnt = 0
    while True:
        cnt += 1
        if cnt**2 == n:
            answer = (cnt+1)**2
            break
        if cnt**2 > n:
            answer = -1
            break
    return answer