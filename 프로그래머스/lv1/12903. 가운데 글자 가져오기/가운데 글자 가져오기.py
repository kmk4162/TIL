def solution(s):
    a = len(s)
    if a % 2 == 0:
        answer = s[int(a/2)-1:int(a/2)+1]
    else:
        answer = s[a//2]
    return answer