def solution(absolutes, signs):
    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] *= -1
    answer = sum(absolutes)
    return answer