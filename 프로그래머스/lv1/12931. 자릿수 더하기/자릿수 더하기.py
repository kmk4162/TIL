def solution(n):
    answer = 0
    for char in str(n):
        answer += int(char)
    return answer