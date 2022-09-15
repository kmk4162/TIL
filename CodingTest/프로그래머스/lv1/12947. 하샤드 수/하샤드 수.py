def solution(x):
    jari = 0
    for i in str(x):
        jari += int(i)
    answer = 0
    if x % jari == 0:
        answer = True
    else:
        answer = False
    return answer