def solution(array, commands):
    answer = []
    for cmd in commands:
        i = cmd[0]
        j = cmd[1]
        k = cmd[2]
        x = array[i - 1 : j]
        x.sort()
        y = x[k-1]
        answer.append(y)
    return answer