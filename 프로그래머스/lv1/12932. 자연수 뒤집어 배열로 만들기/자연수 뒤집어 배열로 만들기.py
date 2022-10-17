def solution(n):
    answer = list(map(int, str(n)))
    result = []
    for i in answer[::-1]:
        result.append(i)
    return result