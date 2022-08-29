def solution(seoul):
    idx = 0
    for name in range(len(seoul)):
        if seoul[name] == 'Kim':
            idx = name
    answer = f'김서방은 {idx}에 있다'
    return answer