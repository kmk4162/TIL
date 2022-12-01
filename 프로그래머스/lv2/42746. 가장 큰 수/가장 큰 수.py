def solution(numbers):
    # 숫자 앞자리 끼리만 비교하면 좋을 듯
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x * 3, reverse = True)
    
    return str(int(''.join(numbers)))
    